#include "cache.hh"
#include "lru_evictor.hh"
#include "fifo_evictor.hh"

#include <boost/program_options.hpp> //This one is the one we reccomend.
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp> //!
#include <boost/beast/version.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/asio/strand.hpp>
#include <boost/asio/dispatch.hpp>
#include <algorithm>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <memory>
#include <string>
#include <thread>
#include <vector>


namespace beast = boost::beast;         // from <boost/beast.hpp>
namespace http = beast::http;           // from <boost/beast/http.hpp>
namespace net = boost::asio;            // from <boost/asio.hpp>
using tcp = boost::asio::ip::tcp;       // from <boost/asio/ip/tcp.hpp>
const auto version = 11;

//NOTE: We are using the Boost.Beast library
//NOTE: Got some inspiration/help for our code from https://www.boost.org/doc/libs/1_66_0/libs/beast/example/http/server/async/http_server_async.cpp
//NOTE: Presuming this link was not lying (https://www.boost.org/doc/libs/develop/libs/beast/example/advanced/server/advanced_server.cpp), only minor changes needed to be made to make this server multithread.

/*
This function (main) receives four optional command line arguments:
 -m maxmem, -s server, -p port, and -t threads. 
 
At this point, you can ignore the thread count and always assume the server runs on localhost (127.0.0.1). 
The maxmem parameter is used to construct the cache, and the port represents the port number to bind to (both should have reasonable defaults in the case they're not provided). Y
You can use getopt, Boost.Program_options, or other libraries to parse the command line.
 Choose reasonable defaults if these values aren't provided. D
 on't use a well-known port number (see here for a list), and prefer a high port number (>2000).
main() then calls whatever functions it needs to set up a cache, and establish a receiving (TCP) socket. 
It then loops indefinitely, listening for messages, processing the requests, and returning the appropriate responses. 
*/




template<
    class Body, class Allocator,
    class Send> //idea gotten from https://www.boost.org/doc/libs/develop/libs/beast/example/http/server/async/http_server_async.cpp

void 
handle_request(http::request<Body, http::basic_fields<Allocator>>&& req,
    Send&& send, Cache& s_cache)
{
    //Error handling section

    // Returns a bad request response
    auto const bad_request =
    [&req](beast::string_view why)
    {
        http::response<http::string_body> res{http::status::bad_request, req.version()};
        res.set(http::field::server, BOOST_BEAST_VERSION_STRING);
        res.set(http::field::content_type, "text/html");
        res.keep_alive(req.keep_alive());
        res.body() = std::string(why);
        res.prepare_payload();
        return res;
    };

    // Returns a not found response
    auto const not_found =
    [&req](beast::string_view target)
    {
        http::response<http::string_body> res{http::status::not_found, req.version()};
        res.set(http::field::server, BOOST_BEAST_VERSION_STRING);
        res.set(http::field::content_type, "text/html");
        res.keep_alive(req.keep_alive());
        res.body() = "The resource '" + std::string(target) + "' was not found.";
        res.prepare_payload();
        return res;
    };

    // Returns a server error response
    auto const server_error =
    [&req](beast::string_view what)
    {
        http::response<http::string_body> res{http::status::internal_server_error, req.version()};
        res.set(http::field::server, BOOST_BEAST_VERSION_STRING);
        res.set(http::field::content_type, "text/html");
        res.keep_alive(req.keep_alive());
        res.body() = "An error occurred: '" + std::string(what) + "'";
        res.prepare_payload();
        return res;
    };
    ///////////
    // Make sure we can handle the method
    if( req.method() != http::verb::get &&
        req.method() != http::verb::head &&
	req.method() != http::verb::put &&
	req.method() != http::verb::post &&
	req.method() != http::verb::delete_){
        std::cout << "Unknown HTTP-method." << std::endl;
        return send(bad_request("Unknown HTTP-method"));
    }
        

    // Request path must be absolute and not contain "..".
    if( req.target().empty() ||
        req.target()[0] != '/' ||
        req.target().find("..") != beast::string_view::npos){
            std::cout << "Illegal request-target" << std::endl;
            return send(bad_request("Illegal request-target"));

        }
        
    // Handle an unknown error
    beast::error_code ec;
    if(ec){
        return send(server_error(ec.message()));
    }
        


    if(req.method() == http::verb::get){// Respond to GET request
        //GET /key: Returns a JSON tuple with { key: , value: } pair (where is the resource in the request, and value is the appropriate value from the cache),
        //or an error message if the key isn't in the cache.

  
	    std::cout << "Get request submitted." << std::endl;
        key_type key = std::string(req.target()); //since we're using key_type as str, we should be able to get away with it?
        key = key.substr(1);
        Cache::size_type holdsize;
        Cache::val_type val = s_cache.get(key, holdsize);
        if(val == nullptr){
	    std::cout << "No value with requested key." << std::endl;
            return send(not_found(req.target()));
        }
        else{
	    std::cout << "Returning desired key/value." << std::endl;
            thread_local http::response<beast::http::string_body> response(http::status::ok, version);
            //response.set(http::field::server, BOOST_BEAST_VERSION_STRING);  //Prep to get string
            response.body() = std::string("\n{\tkey \":") + key + "\",\n\tvalue: \"" + val + "\"\n}\n"; //Need the double quotes and the {} for a JSON object? https://www.w3schools.com/js/js_json_objects.asp 
            response.set(boost::beast::http::field::content_type, "application/json"); //convert from string to jszon
            response.set("val_ptr", val);
            //response.content_length(key.length() + holdsize + 18); //18 because of the character values, esp since the "" are required for json? Counts /0 charcter?
            //response.keep_alive(req.keep_alive());
            //response.prepare_payload();
             response.keep_alive(req.keep_alive());
            response.prepare_payload();
            return send(std::move(response));
            }
        
    }
    else if(req.method() == http::verb::put){ //respond to PUT request
        //PUT /k/v: create or replace a k,v pair in the cache. 
        //You may assume v is always a value and neither k nor v contain the '/' character or any other characters that would invalidate the URL, like a whitespace.
	    std::cout << "Put request submitted." << std::endl;
	    std::stringstream originalsection(std::string(req.target()).substr(1)); //so getline can be used
        //stringstream is NOT thread safe
        std::string key;
        std::string value;
        //Make sure original section does not have characters that would invalidate the URL
        std::getline(originalsection, key, '/'); //Should chop off key from originalsection
        std::getline(originalsection, value, '/');
        key_type altkey = (key_type) key; //const_cast<key_type>(key);
        //Change value to val_type?
        Cache::val_type altvalue = (Cache::val_type) value.c_str();//const_cast<Cache::val_type>(value);
        Cache::size_type givensize = (Cache::size_type) (value.size() +1);//const_cast<Cache::size_type>(value.size());
	std::cout << "Set: key: " << altkey << ", value: " << altvalue << ", size: " << givensize << std::endl;
        s_cache.set(altkey, altvalue, givensize);

        thread_local http::response<http::empty_body> response(http::status::ok, version);
        response.keep_alive(req.keep_alive());
        response.set(http::field::content_type, "text/json");
        response.set("Space-Used", s_cache.space_used());
        response.prepare_payload();
        return send(std::move(response));;

    }
    else if(req.method()== http::verb::post ){ //respond to POST request
        //POST /reset: Upon receiving this message, the server calls Cache::reset to clean up all its data. Any other target than "/reset" should be ignored and return NOT FOUND.
        std::cout << "Post request submitted." << std::endl;
        if(std::string(req.target()) != "/reset"){
		std::cout << "Tried to POST something besides /reset." << std::endl;
                return send(not_found(req.target()));
        }
        std::cout << "Resetting cache." << std::endl;
        s_cache.reset();

        thread_local http::response<http::empty_body> response(http::status::ok, version);
        response.result(http::status::no_content);
        response.keep_alive(req.keep_alive());
        response.set(http::field::content_type, "text/json");
        response.set("Space-Used", s_cache.space_used());
        response.prepare_payload();
        return send(std::move(response));
    } //Only takes reset as a target. For everything else, returns not found
    else if(req.method() == http::verb::delete_){ //respond to DELETE request
        //DELETE /key: Delete from the cache the key and value associated with key.

	    std::cout << "Delete request submitted." << std::endl;

        key_type key = std::string(req.target());
        key = key.substr(1);
        auto isthere = s_cache.del(key);
        
        if(isthere){
            thread_local http::response<http::empty_body> response(http::status::ok, version);
            //response.result(http::status::no_content);
            response.keep_alive(req.keep_alive());
            response.set(http::field::content_type, "text/json");
            response.set("Space-Used", s_cache.space_used());
            response.prepare_payload();
            return send(std::move(response));
        }
        else{
           return send(not_found(req.target())); 
        }

        
        //Assuming we don't need to output anything... done?
    }
    else if(req.method() == http::verb::head){ // Respond to HEAD request
    
        //HEAD: Return just a header, regardless of any resources requested. 
        //The response must include the pair `Space-Used: `, where is the integer value returned by the Cache's `space_used()` method. 
        //You may include as many additional (header) lines as you wish, but as a bare minimum, you should return the HTTP version (1.1 is OK), Accept, and Content-Type with `application/json` (see here). 
        //You can can return these header fields in other types of requests as well, but they must be present in a HEAD request.
	    std::cout << "Head request submitted." << std::endl;
	    Cache::size_type spaceused = s_cache.space_used();

        http::response<http::empty_body> response(http::status::ok, version);
        //res.set(http::field::content_type, mime_type(path));


        response.version(11);   // HTTP/1.1
        response.result(http::status::ok);
        response.set(http::field::content_type, "application/json");
        response.set("Space-Used",spaceused);
        response.keep_alive(req.keep_alive());
        response.prepare_payload();
        return send(std::move(response));


    }
    else{
        //Fail, command is not here?
        return send(bad_request("Unknown request/Method."));
    }

}




//------------------------------------------------------------------------------

// Report a failure
void
fail(beast::error_code ec, char const* what)
{
    std::cerr << what << ": " << ec.message() << "\n";
}

// Handles an HTTP server connection
class session : public std::enable_shared_from_this<session>
{
    // This is the C++11 equivalent of a generic lambda.
    // The function object is used to send an HTTP message.
    struct send_lambda
    {
        session& self_;

        explicit
        send_lambda(session& self)
            : self_(self)
        {
        }

        template<bool isRequest, class Body, class Fields>
        void
        operator()(http::message<isRequest, Body, Fields>&& msg) const
        {
            // The lifetime of the message has to extend
            // for the duration of the async operation so
            // we use a shared_ptr to manage it.
            auto sp = std::make_shared<
                http::message<isRequest, Body, Fields>>(std::move(msg));

            // Store a type-erased version of the shared
            // pointer in the class to keep it alive.
            self_.res_ = sp;

            // Write the response
            http::async_write(
                self_.stream_,
                *sp,
                beast::bind_front_handler(
                    &session::on_write,
                    self_.shared_from_this(),
                    sp->need_eof()));
        }
    };

    beast::tcp_stream stream_;
    beast::flat_buffer buffer_;
    http::request<http::string_body> req_;
    std::shared_ptr<void> res_;
    send_lambda lambda_;
    Cache& serverCache_;

public:
    // Take ownership of the stream
    session(
        tcp::socket&& socket,
        Cache& cache)
        : stream_(std::move(socket))
        , lambda_(*this)
        , serverCache_(cache)
    {
        //serverCache = cache;
    }

    // Start the asynchronous operation
    void
    run()
    {
        // We need to be executing within a strand to perform async operations
        // on the I/O objects in this session. Although not strictly necessary
        // for single-threaded contexts, this example code is written to be
        // thread-safe by default.
        
        net::dispatch(stream_.get_executor(),
                      beast::bind_front_handler(
                          &session::do_read,
                          shared_from_this()));
        //do_read();
    }

    void
    do_read()
    {
        // Make the request empty before reading,
        // otherwise the operation behavior is undefined.
        req_ = {};

        // Set the timeout.
        stream_.expires_after(std::chrono::seconds(30));  //Maybe change this to be unlimited?

        // Read a request
        http::async_read(stream_, buffer_, req_,
            beast::bind_front_handler(
                &session::on_read,
                shared_from_this()));
    }

    void
    on_read(
        beast::error_code ec,
        std::size_t bytes_transferred)
    {
        boost::ignore_unused(bytes_transferred);

        // This means they closed the connection
        if(ec == http::error::end_of_stream){
            return do_close();
        }
            
        if(ec)
            return fail(ec, "read");

        // Send the response
        handle_request(std::move(req_), lambda_, serverCache_);
    }

    void
    on_write(
        bool close,
        beast::error_code ec,
        std::size_t bytes_transferred)
    {
        boost::ignore_unused(bytes_transferred);

        if(ec)
            return fail(ec, "write");

        if(close)
        {
            // This means we should close the connection, usually because
            // the response indicated the "Connection: close" semantic.
            return do_close();
        }

        // We're done with the response so delete it
        res_ = nullptr;

        // Read another request
        do_read();
    }

    void
    do_close()
    {
        // Send a TCP shutdown
        beast::error_code ec;
        std::cout << "Closing another connection." <<std::endl;
        stream_.socket().shutdown(tcp::socket::shutdown_send, ec);
        // At this point the connection is closed gracefully
        stream_.close();
    }
};

//------------------------------------------------------------------------------

// Accepts incoming connections and launches the sessions
class listener : public std::enable_shared_from_this<listener>
{
    net::io_context& ioc_;
    tcp::acceptor acceptor_;
    Cache& listenCache_;

public:
    listener(
        net::io_context& ioc,
        tcp::endpoint endpoint,
        Cache& cache)
        : ioc_(ioc)
        , acceptor_(net::make_strand(ioc))
        , listenCache_(cache) 
    {
        //listenCache_ = cache;
        beast::error_code ec;

        // Open the acceptor
        acceptor_.open(endpoint.protocol(), ec);
        if(ec)
        {
            fail(ec, "open");
            return;
        }

        // Allow address reuse
        acceptor_.set_option(net::socket_base::reuse_address(true), ec);
        if(ec)
        {
            fail(ec, "set_option");
            return;
        }

        // Bind to the server address
        acceptor_.bind(endpoint, ec);
        if(ec)
        {
            fail(ec, "bind");
            return;
        }

        // Start listening for connections
        acceptor_.listen(
            net::socket_base::max_listen_connections, ec);
        if(ec)
        {
            fail(ec, "listen");
            return;
        }
    }

    // Start accepting incoming connections
    void
    run()
    {
        // We need to be executing within a strand to perform async operations
        // on the I/O objects in this session. Although not strictly necessary
        // for single-threaded contexts, this example code is written to be
        // thread-safe by default.
        net::dispatch(
            acceptor_.get_executor(),
            beast::bind_front_handler(
                &listener::do_accept,
                this->shared_from_this()));
        //do_accept();
    }

private:
    void
    do_accept()
    {
        // The new connection gets its own strand
        acceptor_.async_accept(
            net::make_strand(ioc_),
            beast::bind_front_handler(
                &listener::on_accept,
                shared_from_this()));
    }

    void
    on_accept(beast::error_code ec, tcp::socket socket)
    {
        if(ec)
        {
            fail(ec, "accept");
        }
        else
        {
            // Create the session and run it
            std::make_shared<session>(
                std::move(socket), listenCache_)->run();
        }
        // Accept another connection
        std::cout << "Accepting another connection." << std::endl;
        do_accept();
    }
};
//------------------------------------------------------------------------------

namespace po = boost::program_options;

int main(int argc, char* argv[])
{
	// First, read in the optional arguments.
	//
	// Each argument is specified by an option ('-m', '-s', etc.) so that they can come in any order,
	// so long as the maxmem comes after -m and so on and so forth.
	//
	// We can read these options using either getopt(), which is a Linux method, or boost's program_options.
	// Here, we're trying program_options first.
	
	// Create variables with default values
	Cache::size_type maxmem/* = 100*/;
	std::string server_ip/* = "127.0.0.1"*/;
	unsigned short port_number/* = 19134*/; // Chosen because it is 1 more than the port number for Minecraft
	int thread_count/* = 1*/;
        // Declare possible types of command line argument (options)
        po::options_description desc("Available options");
        desc.add_options()
            ("cache-memory,m", po::value<Cache::size_type>(&maxmem)->default_value(100), "Cache size in bytes") //Default is 40 instead of 100 for out test_cache_lib
            ("server-ip,s", po::value<std::string>(&server_ip)->default_value("127.0.0.1"), "IP address of server")
            ("port-number,p", po::value<unsigned short>(&port_number)->default_value(19134), "TCP port number")
            ("thread-count,t", po::value<int>(&thread_count)->default_value(1), "Number of threads")
	    ("help,h", "Produce help message.")
        ;
        

        // Store actual option values from the command line
        po::variables_map vm;
        po::store(po::parse_command_line(argc, argv, desc), vm);
        po::notify(vm);
        
        // Define the desired behavior for each argument.
        // For debugging purposes, these print out the new or default values.
        // In the future, no behavior should need to be designed, since running
        // store and notify should already modify the variables.
        // Mostly for debugging.
        if (vm.count("help")) {
                std::cout << desc << "\n";
                return 0;
            }
        if (vm.count("cache-memory"))
            std::cout << "Cache memory was set to " << vm["cache-memory"].as<Cache::size_type>() << ".\n";
        if (vm.count("server-ip"))
            std::cout << "Server IP was set to " << vm["server-ip"].as<std::string>() << ".\n";
        if (vm.count("port-number"))
            std::cout << "Port number was set to " << vm["port-number"].as<unsigned short>() << ".\n";
        if (vm.count("thread-count"))
            std::cout << "Number of threads was set to " << vm["thread-count"].as<int>() << ".\n";
        if(thread_count <= 0){
            std::cerr << "Bad Parameters "<< std::endl;
            return 1;
        }
        
        
        //Cache currentCache(maxmem); //Set up Cache
        thread_local Cache currentCachePtr(maxmem);
        //auto currentCachePtr = &currentCache; //Need to make into a chared
        std::cout << "A Cache has been created!" << std::endl;
        //server_ip = boost::asio::ip::make_address(vm["server"].as<std::string>());
        auto alt_server_ip = net::ip::make_address(server_ip);
        port_number = vm["port-number"].as<unsigned short>();
        thread_count = vm["thread-count"].as<int>();
        maxmem = vm["cache-memory"].as<Cache::size_type>();        
        
        net::io_context ioc{thread_count};

        // Create and launch a listening port
        std::make_shared<listener>(
            ioc,
            tcp::endpoint{alt_server_ip, port_number},
            currentCachePtr)->run();

        // Run the I/O service on the requested number of threads...
        //May not be infinite?
        std::vector<std::thread> v;
        v.reserve(thread_count -1);
        for(auto i = thread_count - 1; i > 0; --i)
            v.emplace_back(
            [&ioc]
            {
                ioc.run();
            });
        ioc.run();

        //(If we get here, it means we got a SIGINT or SIGTERM)
        // Block until all the threads exit
        for(auto& t : v)
            t.join();

        return EXIT_SUCCESS;

    


}

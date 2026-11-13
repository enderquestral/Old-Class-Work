    //You will need a different Cache constructor that takes the server IP address and port number. I have provided a new cache.hh file that has the new constructor. The constructor will then establish a connection with the server (or exit the program if it fails). Your previous cache_lib.cc can just implement this constructor as empty or assert(false); whereas the cache_client can implement the regular constructor as empty.
    //Your new Cache object should now hold different data: not an actual cache, but rather the wrapper / connection information to access the cache over the network.
    //Just trying to implement cache.hh
//NOTE: Got assistance from https://www.boost.org/doc/libs/develop/libs/beast/example/http/client/sync/http_client_sync.cpp
#include "cache.hh"
#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/version.hpp>
#include <boost/asio/connect.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/convert.hpp>
#include <boost/convert/strtol.hpp>
#include <boost/beast/websocket.hpp>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <tuple>
#include <cassert>
#include <cstring>

namespace beast = boost::beast;     // from <boost/beast.hpp>
namespace http = beast::http;       // from <boost/beast/http.hpp>
namespace net = boost::asio;        // from <boost/asio.hpp>
using tcp = net::ip::tcp;           // from <boost/asio/ip/tcp.hpp>



using storage_unit = std::pair<Cache::val_type, Cache::size_type>;

/////////////
//Cache re-implementation?



class Cache::Impl
{
	// Changed explicit types in unordered_map below to types defined in cache.hh
	
	public:    
    std::string host_; 
    std::string port_;
    net::io_context ioc_;
    mutable tcp::resolver resolver_ = tcp::resolver(ioc_);
    mutable beast::tcp_stream stream_ = beast::tcp_stream(ioc_);
    beast::flat_buffer buffer_;
	int version_ = 11; //or 10 as default?
	mutable std::string stringVal_;
   
    Impl(){
        //assert(false);
	    //abort();
    }

    Impl(std::string host, std::string port){
        host_ = host;
        port_ = port;
        // Look up the domain name
        auto const results = resolver_.resolve(host_, port_); //Should take simple strs?

        // Make the connection on the IP address we get from a lookup
        stream_.connect(results); //Connection refused?
        std::cout << "Got past stream.connect(results)." << std::endl;
    }
    ~Impl(){
         // Gracefully close the socket
    };

	bool del(key_type key) {

        http::request<http::string_body> req{http::verb::delete_, "/"+key, version_}; //version?
        req.set(http::field::host, host_);
        req.set(http::field::user_agent, BOOST_BEAST_VERSION_STRING);

	stream_.connect(resolver_.resolve(host_, port_));

        // Send the HTTP request to the remote host
        http::write(stream_, req); //Problem

        // This buffer is used for reading and must be persisted
        beast::flat_buffer buffer;

        // Declare a container to hold the response
        http::response<http::dynamic_body> res;

        // Receive the HTTP response
        http::read(stream_, buffer, res); //Problem

        //Either get a not_found(false) or a no_content(true)
        auto status = res.result(); //if starts in 4 or 5 something has gone wrong
        if(http::to_status_class(status) == http::status_class::client_error || http::to_status_class(status) == http::status_class::server_error){
	       	//if to_status_class is 4 or 5 then nullptr
	        std::cout << "Pair with key " << key << " was not deleted." << std::endl;
	        return false;
        }
        else{ //if status is a 200
	        std::cout << "Pair with key " << key << " was deleted." << std::endl;
            return true;
        } 
        
	}
	
	void set(key_type key, val_type val, size_type size) {
        //target is key/val
        size +=0; //Maybe don't need to do anything with size?
        std::string KVPair = "/" + std::string(key) +"/"+std::string(val);
        http::request<http::string_body> req{http::verb::put, KVPair, version_}; //version?
        req.set(http::field::host, host_);
        req.set(http::field::user_agent, BOOST_BEAST_VERSION_STRING);

	    stream_.connect(resolver_.resolve(host_, port_));

        // Send the HTTP request to the remote host
        http::write(stream_, req);
        // This buffer is used for reading and must be persisted
        beast::flat_buffer buffer;

        // Declare a container to hold the response
        http::response<http::dynamic_body> res;

        // Receive the HTTP response
        beast::error_code ec;
        http::read(stream_, buffer, res, ec); 
        if(ec && ec != beast::errc::not_connected){
            std::cout << "Error happened in set." << std::endl; 
        }
        
	}
	
	
	val_type get(key_type key, size_type& val_size) const{ //TODO
	    http::request<http::string_body> req{http::verb::get, "/"+key, version_}; //version?
        req.set(http::field::host, host_);
        req.set(http::field::user_agent, BOOST_BEAST_VERSION_STRING);

	    stream_.connect(resolver_.resolve(host_, port_));

	    // Send the HTTP request to the remote host
        http::write(stream_, req); //Problem
	
        // This buffer is used for reading and must be persisted
        beast::flat_buffer buffer;
	
        // Declare a container to hold the response
        http::response<http::dynamic_body> res;
	
        // Receive the HTTP response
        beast::error_code ec;
        http::read(stream_, buffer, res); 
        if(ec && ec != beast::errc::not_connected){
            std::cout << "Error happened in get." << std::endl; 
        }
        
        auto status = res.result(); //if starts in 4 or 5 something has gone wrong
        //std::cout << status << std::endl; 
        if(http::to_status_class(status) == http::status_class::client_error || http::to_status_class(status) == http::status_class::server_error){ //if to_status_class is 4 or 5 then nullptr
            std::cout << "Is not there." << std::endl;
            return nullptr;
        }
        else{ //if status is a 200	    
	        auto origVal = res.at("val_ptr"); //fingers crossed get works
	        stringVal_ = std::string(origVal);
            //std::cout << "The stringVal: " << stringVal_ << std::endl;
            const char* val_p = stringVal_.c_str();
            val_size = stringVal_.length();
            return val_p;  //returning the valptr
        }
	}
    
	size_type space_used() const{ 

        http::request<http::string_body> req{http::verb::head, "/", version_}; //Put anything as target as we don't use it for anything.
        req.set(http::field::host, host_);
        req.set(http::field::user_agent, BOOST_BEAST_VERSION_STRING);

	    stream_.connect(resolver_.resolve(host_, port_));

        // Send the HTTP request to the remote host
        http::write(stream_, req);

        // This buffer is used for reading and must be persisted
        beast::flat_buffer buffer;

        // Declare a container to hold the response
        http::response<http::dynamic_body> res;

        // Receive the HTTP response
        //http::read(stream_, buffer, res);
        
        // Receive the HTTP response
        beast::error_code ec;
        http::read(stream_, buffer, res, ec); 
        if(ec && ec != beast::errc::not_connected){
            std::cout << "Error happened in space_used." << std::endl; 
        } 
        
        auto holdspaceused = res.at("Space-Used");
        //Need to get usedmemory out of the header
        auto space = boost::convert<size_type>(holdspaceused, boost::cnv::strtol());
        return space.get();
	}
	
	void reset(){
        http::request<http::string_body> req{http::verb::post, "/reset", version_}; //version?  '/reset?'
        req.set(http::field::host, host_);
        req.set(http::field::user_agent, BOOST_BEAST_VERSION_STRING);

	    stream_.connect(resolver_.resolve(host_, port_));

        // Send the HTTP request to the remote host
        http::write(stream_, req);

        // This buffer is used for reading and must be persisted
        beast::flat_buffer buffer;

        // Declare a container to hold the response
        http::response<http::dynamic_body> res;

        // Receive the HTTP response
        http::read(stream_, buffer, res); //Read, but don't need to do anything?

	}
};

// Constructor & Destructor:
Cache::Cache(size_type, float, Evictor*, hash_func): pImpl_(new Impl()) {
    assert(false);
    abort();
    //Once again, just having these here so the compiler does not complain.
}
//Assert false this, assert false and crash it. 

Cache::Cache(std::string host, std::string port): pImpl_(new Impl(host, port)){
    
   std::cout << "Cache is being constructed." << std::endl; 
   
    try{
        //Try nothing
    }
    catch(std::exception const& e)
    {
        std::cerr << "Error! : " << e.what() << std::endl;
        //return 1; //Exit failiure
    }
    //return 0; //Exit success    
   

}

Cache::~Cache(){
    
    std::cout << "getting destructed cache" << std::endl;

} //Deconstruct s.t. the port is closed once we no longer are using cache?

// Methods:

void Cache::set(key_type key, val_type val, size_type size) {
	// Description taken from .hh file:
	//
	// Add a <key, value> pair to the cache.
	// If the key is already in the cache, its value gets overwritten by this new one
	// !!! Both the key and the value must be deep-copied, not just pointer-copied
	// If maxmem capacity is exceeded, sufficient (?) values will be removed
	// from the cache to accommodate the new value.
		// "Sufficient" just meaning "satisfying some definition we assign", I think
	pImpl_->set(key, val, size);
}

// Added 'Cache::' to type name since it's defined in the .hh
Cache::val_type Cache::get(key_type key, size_type& val_size) const {
	// Return a pointer to the value associated with the key in the cache; if not found, return null
	// Set the actual size of the returned value (in bytes) in val_size
	return pImpl_->get(key, val_size);
}

bool Cache::del(key_type key) {
	// If an object w/ key 'key' is in the cache, remove it
	return pImpl_->del(key);
}

// Added 'Cache::' to type name since it's defined in the .hh
Cache::size_type Cache::space_used() const {
	// Compute the total amount of memory used by all the current cache values (keys not included)
	return pImpl_->space_used();
}

void Cache::reset(){
	pImpl_->reset();
}


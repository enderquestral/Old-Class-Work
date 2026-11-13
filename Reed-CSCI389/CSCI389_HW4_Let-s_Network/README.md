# HW4-Let's-Network
Hannah Hellerstein and Danny Riso's work on CS 389 HW 4.
#### Notes/Changelogs from HW3:
The test_cache_client was changed from test_cache_lib in that evictor tests were commented out and that everything was moved to a single test case (for ease/clearity regarding cache construction/destruction.) 

### TCP Server:
We primarily just took from the boost documentation for an async http server (https://www.boost.org/doc/libs/1_66_0/libs/beast/example/http/server/async/http_server_async.cpp) and converted it to use our cache_lib. The listener and session classes were almost entirely from the boost documentation. The main used program options to allow the server to read in values from the command line, to change details about the server ip, port number, cache size, and thread count. There was an attempt to make differentiating the different commands into a switch case for efficiency, but that failed. 

### TCP Client: 

[At time of writing, we have a non-optimal solution where the TCP Client must connect at the start of every call. We are working to fix this.]
[If this line still exists, please check either hanwork or dwork afterwards to find our (failed) attempt(s?) to fix this inefficiency.]

For cache_client, we took much of what we did in cache_lib (focusing on Impl) and tried to redo it such that it would connect to and work with a server, without it itself actually having a cache. The Cache constructor (the new one that takes host and post) itself intentionally has basically nothing. Meanwhile, the Impl (which we gave a construtor now that takes host and port from cache) had an overhaul. Impl has objects host, post, ioc, resolver, version, stream, and a mutable string to help with the various calls it must give to the server. Each call has an http::write and then an http::read to send and command messages to the server.
For testing, we remade test_cache_lib into test_cache_client (changing the cache to connect to our server and making sure our server was always set to 40), removing evictor-specific sections since the client could not control that. Result wise, we had a number of very interesting errors at the start, if we did not connect with the stream at the start of every single call. We started with constant "end of stream" errors, then constant "broken pipes," and the occasional "segfault." Most interestingly, in client, we found that http::write would work most of (not all of) the time, while the http::read would not work at all. We eventually fixed this by forcefully connecting at the start of every call.
Get was a special case, in that we needed to a special mutable string to the impl such that the returned pointer wouldn't immediately go out of scope. 

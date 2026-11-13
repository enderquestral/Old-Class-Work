# HW5-Lies-statistics-and-benchmarks  
Hannah Hellerstein and Danny Riso's work on CS 389 HW6.  

#### Notes/Changelogs from HW5:  

N/A.

### Part 1: Multi-threaded benchmark (50%)
Then, create two graphs and include them in your README, one showing the aggregate throughput as a function of the number of worker threads (nthread), and another showing the 95th-latency as a function of nthreads. (If you know how, you may combine those into a single graph with two different y-axes.) Identify the saturation point and report your maximum unsaturated throughput and latency. This is your new performance baseline.

Note: We tried to use the baseline we had before in HW5, which was a cache size of 10000 with a nreq size of 250000. However, we worried that the nreq size was too large for this, and so we dropped it to 100000. This was also running on a one-core-dedicated VM, so we couldn't test for too many threads. We then suspect that 9 threads is when things started to get tricky for the VM, and so seemed to have multiple varying results for it. We suspect 9 threads will be the point of saturation.

![Graph of multithreaded client performance with a singlethreaded server](/baseline_performance.png)

As the number of threads increases, the throughput levels out around 35,000 requests per second, making that the likely saturation point. The latency time changed very little throughout the trials, consistently around 0.55 milliseconds. From these results, we estimate the saturation point to be at 4 threads, where the latency is 0.549 milliseconds and the throughput is 33,377.8 requests per second.

### Part 2: Multithreaded Server (50%)

From the tests carried out on the cache with a multithreaded performance, we found a sizable boost in performance when the server was able to respond to multiple requests simultaneously, even with locks employed. The tests had to be carried out with the server and client running on the same machine, causing some performance dips at higher thread counts as the server and client competed for CPU resources.

From our results, we predict that the saturation point with both multithreaded server and client occurs at 12 threads split between the client and the server. When 4 threads are reserved for the client, the server demonstrates a fairly consistent performance increase with additional server threads, while an 8-threaded client starts seeing significant degradation of performance beyond 4 server threads.

Regardless, multithreading the server results in a massive performance boost, as the throughput increases from an average 35,000 requests per second to 100,000 requests per second. Throughout, the mean latency is consistently around 0.5 ms.

Consistently running a server with 3 threads, client performance is as follows:
![Graph of client performance with a multithreaded server](/client_performance.PNG)
Compared to the client's performance with a single-threaded server, running the server with 3 threads resulted in the most representative performance boost, though with some dips as the client and server began competing with higher number of client threads.


Running a client with 1, 4, and 8 threads, server performance is as follows:
![Graph of server performance with a singlethreaded client](/server_performance_1c.PNG)
![Graph of server performance with a multithreaded client](/server_performance_4c.PNG)
![Graph of server performance with a multithreaded client](/server_performance_8c.PNG)

All of these graphs demonstrate the performance improvement granted by using a multithreaded server, as the throughput massively increases when using a multi-threaded server rather than a single-threaded.

When the client only has 1 thread, it can only send so many requests. Running a server with additional threads improves performance to a point, but beyond 6 server threads, the performance dips as server threads spend more time waiting for requests than responding to them.

Running the client with both 4 and 8 threads demonstrate the multithreaded server's capability, as the throughput increases in both graphs as the number of server threads increases, only dipping a little with 6 server threads due to competing for CPU resources.


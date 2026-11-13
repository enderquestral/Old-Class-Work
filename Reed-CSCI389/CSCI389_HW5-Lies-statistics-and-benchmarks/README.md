# HW5-Lies-statistics-and-benchmarks  
Hannah Hellerstein and Danny Riso's work on CS 389 HW 5.  
#### Notes/Changelogs from HW4:  
-Took inspiration from Eitan's [eitanf] code (thank you!) such that our client and server code was changed to allow for a stream\_ connection only once in the client constructor. This was done because it was believed that having this consistant connection would allow for easier measurements in this assignment.  
-For Usage: Call the makefile. Then, run ./cache_server -m 10000 in one terminal (10000 being our chosen cache fixed size) and either ./simple_client or ./baseline_client 250000 (depending on performance measurements or not, with 250000 being our baseline number of requests). 

### Part 1: Workload generation (40%)
Our workload generator employs two public functions. One randomly generates whether a delete, set, or get request will be generated later on following the approximate frequency ratios given in the Memcached workload paper: 67% get, 31% delete, and 2% set requests. In later testing, we'll see if adjusting the percentage of set and delete requests generated assists in producing a more representative hit rate.

The second public function randomly generates key and value strings to be set, get, or deleted from the cache. It does so first by generating the lengths of these numbers (also approximating the results of the Memcached paper with an Extreme Value Distribution for keys and a Geometric Distribution for values), and then by calling a helper function to generate a random string of a specified length.

To allow key reuse, we implemented pools of pregenerated keys and values, both so the workload generator would not constantly generate invalid keys and so performance measurements would not be hindered by generating a key upon every request to the cache.

To allow key reuse, we implemented pools of pregenerated keys and values, both so the workload generator would not constantly generate invalid keys and so performance measurements would not be hindered by generating a key upon every request to the cache.

Every request call (generating set, get, and del values) selects from a pool randomly. At a cache size of 11000, our cache is first warmed up so that 10000 of the cache is filled, and then every subsequent request selects from each pool uniformly, consistently producing a hit rate between 75 and 85 percent.

### Part 2: Baseline latency and throughput (40%)
Our Chosen nreq: 250000. We chose this because this ran in a reasonable amount of time (40 seconds) and subsequent calls had 95th-percentile latency and Requests per second measurements within 5% difference. This was done on a 2.3 GHz Dual-Core Intel Core i5, 8GB Memory MacBook Pro. OS was a Ubinutu VM.

Below, find the plot of the distribution of latencies, for nreq = 250000.

![Part 2 Latency Test Histogram](/latency_hist.png "Latency Histogram")

### Part 3: Sensitivity testing (20%)
By performance they mean: Get 95th latency and mean throughput.  
Note: Unless stated explicitly otherwise, nreq = 250000 for all these tests. Similarly, unless stated otherwise, a Cache Size of 10000.

#### Analysis
We examined how the 95th-percentile latency and throughput varied across architectures, compilers, load factors, and eviction policies.

Varying the load factor of the underlying cache did not have a significant effect on either value. This indicates that the size of the cache, and thus the time required for collision handling and resizing, are not slow enough to impact the time needed to send a request.

For the most part, the 95th-percentile latency was constant across all the experimentation save for the compiler, for which g++-8 and clang++ demonstrated a slight improvement. We predict this is likely due to optimization procedures employed by the different compilers, which made either the requests themselves or the transmission of them faster when compared to the older compiler, g++.

Meanwhile, the requests handled per second demonstrated a notable variation across every factor except for load factor.  
The architecture variance is fairly easily explained; the Windows desktop has more cores, more memory, and more power overall than the MacBook, enabling it to handle requests faster. 
 
From the compiler results, where g++-8 demonstrates the fastest latency time but the least requests per second, it's likely that while more of the requests are optimized to be handled faster, the requests that do take longer are slow enough to weigh down the mean throughput. Thus, to optimize performance, clang++ demonstrates the best results, with a low 95th-percentile latency as well as a decently high throughput.  

The eviction policy results demonstrate that the overhead required in implementing an eviction policy significantly affects the time to handle each request. Especially considering that eviction is only called into use while setting a new value, and set functions are only called 2% of the time, our LRU implementation drastically decreases the average number of requests handled per second. The greatest number of requests handled per second comes from not implementing an evictor at all, which makes sense since it entails that all set operations are declined once the cache is filled, innately reducing how long set requests take. Thus, the best performance comes from implementing a FIFO evictor so that new values are still being added to the cache without drastically slowing down request handling.

#### Architecture: VM vs. Mac vs. Windows 
Both the VM and the Mac were done on a 2.3 GHz Dual-Core Intel Core i5, 8GB Memory MacBook Pro. The Windows was done on a AMD Ryzen 7 2700 Eight-Core Processor 3.20 GHz, 16 GB desktop.

VM:  
95th-percentile latency: 0.569012  
Requests per second: 37610.953125  

Mac:  
95th-percentile latency: 0.575764  
Requests per second: 36095.871094  

Windows:  
95th-percentile latency: 0.568379  
Requests per second: 83699.691406  


#### Compilers: g++ vs. g++-8 vs. clang++
Note: These were all run in the Ubnutu VM, with hardware specs seen above. 

g++:  
95th-percentile latency: 0.573778  
Requests per second: 75528.703125  

g++-8:  
95th-percentile latency: 0.480523  
Requests per second: 43630.187500  

clang++:  
95th-percentile latency: 0.502745  
Requests per second: 69252.078125  

#### Load Factor: 0.75 baseline vs. 0.5 through 0.9 in 0.1 intervals

0.5:  
95th-percentile latency: 0.579197  
Requests per second: 58752.335150  

0.6:  
95th-percentile latency: 0.578637  
Requests per second: 55159.460682  

0.7:  
95th-percentile latency: 0.5789735  
Requests per second: 55752.35091  

0.75:  
95th-percentile latency: 0.575617   
Requests per second: 59589.17513  

0.8:  
95th-percentile latency: 0.578898  
Requests per second: 61674.31758  

0.9:  
95th-percentile latency: 0.588776  
Requests per second: 52964.255830  

#### Eviction policy: None baseline vs. FIFO vs. LRU

None:  
95th-percentile latency: 0.572191   
Requests per second: 90800.77453  

FIFO:  
95th-percentile latency: 0.566468  
Requests per second: 89576.640631  

LRU:  
95th-percentile latency: 0.585424  
Requests per second: 63582.35546  

#include <iostream>
#include "cache.hh"
#include "workload_generator.hh"
#include <stdint.h>



using performance = std::tuple<double, float>;
using segments = std::chrono::duration<float, std::milli>;
/* From assignment description:
 * Create a new benchmark program (that can be entirely based on your driver from part 1). 
 * Write a function called baseline_latencies that takes at least one parameter nreq and returns a vector of nreq measurements. 
 * Each measurement is the time, in milliseconds, that a random Cache request took, based on your workload generator (the request can be any of the three types).
*/

std::vector<float> baseline_latencies(int nreq){
   auto cache = Cache("127.0.0.1","19134");
   Cache::size_type tempvalsize;
   int numberofthingsgenerated = 1000;
   std::vector<float> givenvector;
   auto WorkloadGenerator = workload_generator(numberofthingsgenerated);
   WorkloadGenerator.warmup_cache(cache);

   for (int i = 0; i < nreq; i++)
   {
    switch (WorkloadGenerator.case_generator())
    {
        case workload_generator::req_type::set:
	    {
            auto getcomplete = WorkloadGenerator.request_inputs_generator_set();
	    auto key = std::get<0>(getcomplete);
	    auto value = std::get<1>(getcomplete);
	    auto value_size = std::get<2>(getcomplete);

            std::chrono::time_point start = std::chrono::high_resolution_clock::now(); //start timing
            cache.set(key, value, value_size);
            std::chrono::time_point finish = std::chrono::high_resolution_clock::now(); //end timing

            givenvector.push_back(segments(finish-start).count());
            break;
	    }

        case workload_generator::req_type::del:
	    {
            auto givedelrequirements = WorkloadGenerator.request_inputs_generator_del();

            std::chrono::time_point start = std::chrono::high_resolution_clock::now(); //start timing
            cache.del(givedelrequirements);
            std::chrono::time_point finish = std::chrono::high_resolution_clock::now(); //end timing
            
            givenvector.push_back(segments(finish-start).count());
            break;
	    }
        
        case workload_generator::req_type::get:
	    {
            auto givegetrequirements = WorkloadGenerator.request_inputs_generator_get();  
            
            std::chrono::time_point start = std::chrono::high_resolution_clock::now(); //start timing
            cache.get(givegetrequirements, tempvalsize);
            std::chrono::time_point finish = std::chrono::high_resolution_clock::now(); //end timing
            
            givenvector.push_back(segments(finish-start).count());
            break;
	    }
    }
    }
   return givenvector;

}

/* From assignment description:
 * Wrap the baseline_latencies function with another function called baseline_performance.
 * This function returns two values: the 95th-percentile latency (that is, what is the number that is above exactly 95% of all your measurements), and the mean throughput, defined as requests per second, of your benchmark.
*/

performance baseline_performance(int nreq){
    auto performancedata = baseline_latencies(nreq);
    
    // Print time taken for each request
    for (float i : performancedata)
        std::cout << i << std::endl;

    std::sort(performancedata.begin(), performancedata.end());
    int Index = (int)ceil((95.0/ 100.0) * (double)performancedata.size());
    auto nintyfifthpercentilel= performancedata[Index-1];

    double totaltimeforallrequests = 0.0; //in miliseconds
    std::for_each(performancedata.begin(), performancedata.end(), [&] (int n) {
        totaltimeforallrequests += n;
    });
    
    auto totaltimeratio = ( nreq / totaltimeforallrequests) * 1000; //In seconds

    performance holdvalues(nintyfifthpercentilel, totaltimeratio); //for all requests
    return holdvalues;

}


int main(int argc, char* argv[]){
    if (argc != 2)
    {
        std::cout << "Required arguments: nreq (int) " <<'\n';
        exit(-1);
    }
    auto nreq = std::stoi(argv[1]);

    std::cout << "Baseline performance test: " <<  std::endl; 
    auto givenpreformance = baseline_performance(nreq);
    std::cout << "95th-percentile latency: " << std::to_string(std::get<0>(givenpreformance)) << std::endl; 
    std::cout << "Requests per second: " << std::to_string(std::get<1>(givenpreformance)) << std::endl; 

    exit(0);
}

#include <iostream>
#include "cache.hh"
#include "workload_generator.hh"
#include <stdint.h>
#include <vector>
#include <future>
#include <thread>
#include <mutex>
//#include <boost/thread.hpp>
//#include <boost/fiber/future/future.hpp>
//#include <boost/thread/future.hpp>
//#include <boost/make_shared.hpp>

//auto cache = Cache("127.0.0.1","19134"); //Maybe need to get rid of this?
const int numberofthingsgenerated = 1000; //Should change depending on cache size 
auto WorkloadGenerator = workload_generator(numberofthingsgenerated);

using performance = std::tuple<double, float>;
using segments = std::chrono::duration<float, std::milli>;
float num_gets = 0;
float num_hits = 0;

std::mutex get_mutex;
std::mutex time_mutex;
std::mutex performance_mutex;


std::vector<float> baseline_latencies(int nreq){
    //Make most everything here in this function const or thread local.

    //Make this run in an independent thread, and run several of these.
    //Make sure that the function is thread-safe (does not modify any state that isn't private to function/thread).
    //auto WorkloadGenerator = workload_generator(numberofthingsgenerated);
   thread_local auto cache = Cache("127.0.0.1","19134"); //Maybe need to get rid of this?
    WorkloadGenerator.warmup_cache(cache);
   thread_local Cache::size_type tempvalsize;
   thread_local std::vector<float> givenvector;
   //float meantime;
   for (int i = 0; i < nreq; i++)
   {
        

    switch (WorkloadGenerator.case_generator()) //of first thing, tells us which thing we are doing and what we are asking for in second function
    {
        case workload_generator::req_type::set:
	    {   //case set
            //Set needs: key, value, value size
            //std::cout << "3. Call ";
            auto getcomplete = WorkloadGenerator.request_inputs_generator_set();
	        auto const key = std::get<0>(getcomplete);
	        auto const value = std::get<1>(getcomplete);
	        auto const value_size = std::get<2>(getcomplete);

            std::chrono::time_point const start = std::chrono::high_resolution_clock::now(); //start timing
            cache.set(key, value, value_size);
            std::chrono::time_point const finish = std::chrono::high_resolution_clock::now(); //end timing
            //meantime = std::chrono::duration_cast<std::chrono::microseconds>(finish - start).count();

	        

	        //std::cout << "Set {" << key << ", " << value << "} with size " << std::to_string(value_size) << "." << std::endl;
            //givenvector.push_back(meantime);
            time_mutex.lock();
            givenvector.push_back(segments(finish-start).count());
            time_mutex.unlock();
            break;
	    }

        case workload_generator::req_type::del:
	    {   //case del
            //Only needs a key
            //std::cout << "2. Call ";
            auto givedelrequirements = WorkloadGenerator.request_inputs_generator_del();
            std::chrono::time_point const start = std::chrono::high_resolution_clock::now(); //start timing
            cache.del(givedelrequirements); //Outputs a bool, not sure we're to do anything with it.
            std::chrono::time_point const finish = std::chrono::high_resolution_clock::now(); //end timing
            //meantime = std::chrono::duration_cast<std::chrono::microseconds>(finish - start).count();


	        
            
	        //std::cout << "Del {" << givedelrequirements << "}. Deleted: " << deleted << std::endl;
            //Ask workload_request_inputs_generator for suitable things to input on the given call
            //givenvector.push_back(meantime);
            time_mutex.lock();
            givenvector.push_back(segments(finish-start).count());
            time_mutex.unlock();
            break;
	    }
        
        case workload_generator::req_type::get:
	    {   //case get
            //Needs a key, and a valsize to pass in (but we don't need to assign anything)
            //std::cout << "1. Call ";
            get_mutex.lock();
	        num_gets += 1;
            get_mutex.unlock(); 
            auto givegetrequirements = WorkloadGenerator.request_inputs_generator_get();  
            std::chrono::time_point const  start = std::chrono::high_resolution_clock::now(); //start timing
            auto get_results = cache.get(givegetrequirements, tempvalsize);
            std::chrono::time_point const finish = std::chrono::high_resolution_clock::now(); //end timing
            //meantime = std::chrono::duration_cast<std::chrono::microseconds>(finish - start).count();

	    if (get_results != nullptr){
            get_mutex.lock();
            num_hits += 1;
            get_mutex.unlock();
        }
		    
	        //std::cout << "Get {" << givegetrequirements << "}.";
            //givenvector.push_back(meantime);
            time_mutex.lock();
            givenvector.push_back(segments(finish-start).count());
            time_mutex.unlock();
	    
            //Ask workload_request_inputs_generator for suitable things to input on the given call
            break;
	    }
    }
    //givenvector.push_back(meantime);
    }
   //return givenvector;
   return givenvector;

}



/*
Wrap the baseline_latencies function with another function called baseline_performance. 
This function returns two values: the 95th-percentile latency (that is, what is the number that is above exactly 95% of all your measurements), and the mean throughput, defined as requests per second, of your benchmark.
*/
performance baseline_performance(int nreq){
    auto performancedata = baseline_latencies(nreq);
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

performance threaded_performance(int nthreads, int nreq){
    //launch nthreads worker threads that take nreq synchronous requests and return the resulting vector of latencies. 
    // finds the 95th percerntile latency of ALL these latencies combined, as well as the combined throughput of all threads
    //WorkloadGenerator.warmup_cache(cache);
    //std::vector<std::thread> vector_of_threads;
    std::vector<std::vector<float>> holdlatencyvectors;
    //std::vector<boost::thread> z; //May need to not make this a ptr
    //May want to make the ptrs shared_ptrs for safetys sake
    for (int i = 0; i < nthreads; ++i){

        //Future should be an independent thread
        auto future = std::async(std::launch::async, baseline_latencies, nreq); //Should help with thread safety

        thread_local std::vector<float> simple = future.get();

        //std::cout << simple <<std::endl;

        //for(long unsigned i=0; i < simple.size(); i++)
        //    std::cout << simple.at(i) << ' ';
        performance_mutex.lock();
        holdlatencyvectors.push_back(simple);
        performance_mutex.unlock();
        /*boost::packaged_task<std::vector<float>> task{boost::bind(baseline_latencies, nreq)};
        boost::unique_future<std::vector<float>> f = task.get_future();
        boost::thread t {std::move(task)};
        std::cout << std::to_string(f.get()) << '\n';*/

        ///holdlatencyvectors.push_back(newvector);
        //delete z[i]; //??
    }
        //z.push_back(new boost::thread(baseline_latencies(nreq)));

    //Somehow need to get the output from a thread

    //boost::promise<int> p;
    
    //std::vector<float> newvector = p.get_future().get(); //This will block until the promise is set.
    
    double  nintyfifthpercentilel= 0.0; 
    double totaltimeforallrequests = 0.0; //in miliseconds
    //std::vector<float> hold95th;
    for (unsigned i = 0; i < holdlatencyvectors.size(); i++)
    {
        auto performancedata = holdlatencyvectors[i];
        std::sort(performancedata.begin(), performancedata.end());
        std::for_each(performancedata.begin(), performancedata.end(), [&] (int n) {
            totaltimeforallrequests += n;
        });

        int Index = (int)ceil((95.0/ 100.0) * (double)performancedata.size()); 
        nintyfifthpercentilel += performancedata[Index-1];
    }
    nintyfifthpercentilel = nintyfifthpercentilel /holdlatencyvectors.size(); //avg of each latency vector

    auto totaltimeratio = ( (nreq * nthreads) / totaltimeforallrequests) * 1000; //In seconds 
    performance holdvalues(nintyfifthpercentilel, totaltimeratio); //for all requests
    return holdvalues; 

}

int main(int argc, char* argv[]){
    if (argc != 3)
    {
        std::cout << "Required arguments: nreq (int), nthreads (int) " <<'\n';
        exit(-1);
    }
    auto nreq = std::stoi(argv[1]);
    auto nthreads = std::stoi(argv[2]);


    std::cout << "Baseline performance test: " <<  std::endl; 
    //auto givenpreformance = baseline_performance(nreq);
    auto givenpreformance = threaded_performance(nthreads, nreq);

    std::cout << "95th-percentile latency: " << std::to_string(std::get<0>(givenpreformance)) << std::endl; 
    std::cout << "Requests per second: " << std::to_string(std::get<1>(givenpreformance)) << std::endl;
    //std::cout << "Num_Hits: " << std::to_string(num_hits) << std::endl;
    //std::cout << "Num_Gets: " << std::to_string(num_gets) << std::endl;
    std::cout << "Hit rate: " << std::to_string(num_hits / num_gets) << std::endl;
    //std::cout << "Total throughput: " << std::endl;
    exit(0);
}
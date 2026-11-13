#include <iostream>
#include "cache.hh"
#include "workload_generator.hh"

using performance = std::tuple<double, float>;


int main(){
    //create a cache in here
    //ask workload generator what to do with it,
    // get info from workload_generator, use that information to command cache_client to do something

    //Create measurements for hit rate
    float totalnumbergetrequests = 0;
    float totalnumberdelrequests = 0;
    float totalnumbersetrequests = 0;
    float totalnumbergethits = 0;

    int numberofthingsgenerated = 50; //Arbitrary number for pool sizes
    auto WorkloadGenerator = workload_generator(numberofthingsgenerated);

    Cache::size_type tempvalsize;
    auto cache = Cache("127.0.0.1","19134");
    

    WorkloadGenerator.warmup_cache(cache);
    auto count = 1000; // Number of requests to generate and send to server

    for (int i = 0; i < count; i++)
    {
        switch (WorkloadGenerator.case_generator())

        {
        case workload_generator::req_type::set:
        {
            totalnumbersetrequests +=1;
            auto getcomplete = WorkloadGenerator.request_inputs_generator_set();

            auto key = std::get<0>(getcomplete);
            auto value = std::get<1>(getcomplete);
            auto value_size = std::get<2>(getcomplete);
            cache.set(key, value, value_size);

            break;
        }

        case workload_generator::req_type::del:
        {
            totalnumberdelrequests +=1;
            auto givedelrequirements = WorkloadGenerator.request_inputs_generator_del();
            cache.del(givedelrequirements);
            break;
        }

        case workload_generator::req_type::get:
        {
            totalnumbergetrequests +=1;
            auto givegetrequirements = WorkloadGenerator.request_inputs_generator_get();
            auto callgetresults = cache.get(givegetrequirements, tempvalsize);

            if (callgetresults != nullptr)
            {
                totalnumbergethits +=1;
	    } 
            break;
        }
    }
    
    
    }


    //After loop: report hit rate. Then finish.
    std::cout << "Total number of get calls to total calls: " << std::to_string(totalnumbergetrequests /count) <<std::endl;

    std::cout << "Number of gethits:  " << std::to_string(totalnumbergethits) <<std::endl;
    std::cout << "Number of get requests:  " << std::to_string(totalnumbergetrequests ) <<std::endl;
    std::cout << "Number of set requests:  " << std::to_string(totalnumbersetrequests ) <<std::endl;
    std::cout << "Number of del requests:  " << std::to_string(totalnumberdelrequests ) <<std::endl;

    std::cout << "Hit rate: " << std::to_string(totalnumbergethits / totalnumbergetrequests ) <<std::endl;

    exit(0);
}

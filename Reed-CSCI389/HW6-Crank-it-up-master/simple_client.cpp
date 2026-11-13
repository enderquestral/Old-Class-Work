#include <iostream>
#include "cache.hh"
#include "workload_generator.hh"



using performance = std::tuple<double, float>;


int main(){
    //create a cache in here
    //ask workload generator what to do with it,
    // get info from workload_generator, use that information to command cache_client to do something


    //Have it send one request at a time, but perhaps structure it such that it is prepared to take/run multiple inputs
    //measure how many of the get requests were hits, and how many were misses. At the end of the run, it can report the cache's hit rate.

    //Create measurement for hit rate
    float totalnumbergetrequests = 0;
    float totalnumberdelrequests = 0;
    float totalnumbersetrequests = 0;
    float totalnumbergethits = 0;
    //std::default_random_engine generator;
    //std::vector<key_type> key_pool;
    //std::vector<std::string> val_pool;
    int numberofthingsgenerated = 50; //Arbitaray number
    auto WorkloadGenerator = workload_generator(numberofthingsgenerated);
    

    Cache::size_type tempvalsize;
    auto cache = Cache("127.0.0.1","19134");
    //Set server to be around 1100
    
    WorkloadGenerator.warmup_cache(cache);  //may not need?
    //int seed = 10; //A seed to set the generators to in order to maybe make things more reproducible? can change later
    auto count = 1000; //change this for easier testing later
    //for loop here
   
    
    for (int i = 0; i < count; i++)
    {
        //Ask case_generator for command
        //auto command = workload_generator();
        //Put into switch case to do a thing
        switch (WorkloadGenerator.case_generator()) //of first thing, tells us which thing we are doing and what we are asking for in second function
        {
        case workload_generator::req_type::set:
	{   //case set
            //Set needs: key, value, value size
            totalnumbersetrequests +=1;
	    std::cout << "3. Call ";
            auto getcomplete = WorkloadGenerator.request_inputs_generator_set();
	    auto key = std::get<0>(getcomplete);
	    auto value = std::get<1>(getcomplete);
	    auto value_size = std::get<2>(getcomplete);
            cache.set(key, value, value_size);
	    std::cout << "Set {" << key << ", " << value << "} with size " << std::to_string(value_size) << "." << std::endl;

            break;
	}

        case workload_generator::req_type::del:
	{   //case del
            //Only needs a key
            totalnumberdelrequests +=1;
	    std::cout << "2. Call ";
            auto givedelrequirements = WorkloadGenerator.request_inputs_generator_del();
            auto deleted = cache.del(givedelrequirements); //Outputs a bool, not sure we're to do anything with it.
	    std::cout << "Del {" << givedelrequirements << "}. Deleted: " << deleted << std::endl;
            //Ask workload_request_inputs_generator for suitable things to input on the given call
            break;
	}
        
        case workload_generator::req_type::get:
	{   //case get
            //Needs a key, and a valsize to pass in (but we don't need to assign anything)
            /* code */
	    std::cout << "1. Call ";
            totalnumbergetrequests +=1;
            auto givegetrequirements = WorkloadGenerator.request_inputs_generator_get();
            auto callgetresults = cache.get(givegetrequirements, tempvalsize);
	    std::cout << "Get {" << givegetrequirements << "}.";
            if (callgetresults != nullptr)
            {
                totalnumbergethits +=1;
		std::cout << " Hit." << std::endl;
            } else {
		std::cout << " Miss." << std::endl;
	    }
            
            //Ask workload_request_inputs_generator for suitable things to input on the given call
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
    std::cout << "Space-used: " << std::to_string(cache.space_used() ) <<std::endl;
    
    exit(0);
}

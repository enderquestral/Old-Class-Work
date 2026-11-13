#include "workload_generator.hh"

// This file implements a class and its methods that are used for the performance tests
// on the client-server cache implementation.
// Its functionality includes generating a random type of request (between GET, SET, and DEL),
// generating a string of a certain length, and generating lengths of particular distributions,
// among other helper functions.
//
// Overall, it serves the purpose of randomly generating a type of request for an action to be taken on a cache,
// as well as the parameters passed into said request.

using fullset = std::tuple<key_type, Cache::val_type, Cache::size_type>;
//30:1 gets to sets, 85% hit rate

workload_generator::workload_generator(int poolsizes)
        : generator_(std::default_random_engine(std::chrono::system_clock::now().time_since_epoch().count())) {
    fill_pool_key(poolsizes);
    fill_pool_val(poolsizes);
}


workload_generator::req_type workload_generator::case_generator(){
    std::uniform_real_distribution<> distribution(0,1);
    auto randomaction = distribution(generator_);
    if (randomaction <= set_number_) //If randomaction <= [some number], make it set.
    {
        //Fraction: 2/90
	std::cout << "Randomly generated set." << std::endl;
	return req_type::set;
    }
    else if (randomaction <= del_number_)//Else If randomaction <= [some other number], make it del
    {
        //Fraction: 14/45
 	std::cout << "Randomly generated del." << std::endl;
	return req_type::del;
    }
    else //Else, make it get
    {
        //Fraction: 2/3
 	std::cout << "Randomly generated get." << std::endl;
	return req_type::get;
    }
}


std::string workload_generator::generate_a_string(int inputsize){
    //generate a string x by generating random characters inputsize number of times, based on their ascii values
    // A weighted extreme value distribution is implemented in order to limit the number of
    // possible strings generated to increase hit rate.
    // Converting the number into an int between 33 and 126 ensures the result is a valid ASCII character.
    std::string newstring;
    std::extreme_value_distribution<> chardistribution(50, 5);
    for (int i = 0; i < (inputsize - 1); i++){
        auto chara = ((static_cast<int>(chardistribution(generator_)) % (126 - 33)) + 33);
        char newitem = (char) chara;
        newstring+=(newitem);
    }
    return newstring;
}

int workload_generator::generate_length(data_type type) {
        int length = 0;
        if (type == data_type::key){
                // An extreme value distribution is selected for generating a key length
                // in order to approximate the distribution of keys tested
                // in the Workload Analysis paper.
                std::extreme_value_distribution<> distribution(30, 5);
                length = static_cast<int>(distribution(generator_)) +1; //So a len of 0 cannot happen.
        } else if (type == data_type::value) {
                // An exponential distribution, as well as the value it is multiplied by,
                // were both chosen to approximate the workload tested in the paper.
                std::exponential_distribution<> distribution;
                auto exp_mult_placeholder = 100;
                length = static_cast<int>(distribution(generator_) * exp_mult_placeholder);
        }
        return length;
}



fullset workload_generator::request_inputs_generator_set(){
    // A normal distribution is used to select keys from the previously generated pool
    // in order to simulate key reuse at frequencies shown in the paper.
    std::normal_distribution<> key_distribution(key_pool_.size()/2, 1.0);
    auto key_spot = static_cast<int>(std::round(key_distribution(generator_)));
    auto key = key_pool_[key_spot];

    // A uniform distribution is used to select values from the previously generated pool
    // under the assumption that value reuse is not relevant to performance.
    std::uniform_int_distribution<int> val_distribution(0,val_pool_.size());
    auto val_spot = static_cast<int>(std::round(key_distribution(generator_)));
    value_s_ = val_pool_[val_spot];

    std::cout << "Set generated " << key_spot << " and " << val_spot << std::endl;

    Cache::val_type value = value_s_.c_str();
    Cache::size_type val_size = static_cast<Cache::size_type> (value_s_.size());
    fullset response = std::make_tuple(key, value, val_size);
    return response;
}

key_type workload_generator::request_inputs_generator_del(){
    // An exponential distribution is used to select very few particular keys.
    // This selectivity reduces the number of invalidation misses during performance tests.
    std::exponential_distribution<> distribution(6.2);
    auto key_spot = static_cast<int>( std::round(distribution(generator_)));
    std::cout << "Del generated " << key_spot << std::endl;
    auto givenspot = key_pool_[key_spot];
    return givenspot;
}

key_type workload_generator::request_inputs_generator_get(){
    // An exponential distribution is used to select keys for get requests
    // in order to simulate the trend demonstrated in the paper,
    // where 50% of keys are used in 99% of requests, while the other 50% make up the other 1%.
    std::exponential_distribution<> distribution(0.15);
    auto key_spot = (static_cast<int>(std::round(distribution(generator_)))) % key_pool_.size(); //Mod-ing it so we can't go out of scope
    std::cout << "Get generated " << key_spot << std::endl;
    return key_pool_[key_spot];
    
}

void workload_generator::fill_pool_key(int generatenumber){
    for (int i = 0; i < generatenumber; i++)
    {
        int length = generate_length(data_type::key);
        key_pool_.push_back(generate_a_string(length));
    }
}

void workload_generator::fill_pool_val(int generatenumber){
    for (int i = 0; i < generatenumber; i++)
    {
        int length = generate_length(data_type::value);
        val_pool_.push_back(generate_a_string(length));
    }
}

void workload_generator::warmup_cache(Cache& cache){

	std::cout << "Warming up." << std::endl;
    //Fill a percentage of cache size with stuff to produce more representative results in tests
    unsigned int cache_size = 10000;

    // Trying to implement a for loop rather than for-each to avoid seg faults
    /*
    for (unsigned int i = 0; i < key_pool_.size(); ++i) {
	auto key = key_pool_[i];
	fullset getcomplete = request_inputs_generator_set();
	// If we're still seg faulting, the problem might be calling rig_s too many times or something
	if ((cache.space_used() + std::get<2>(getcomplete)) > cache_size)
		break;
	cache.set(key, std::get<1>(getcomplete), std::get<2>(getcomplete));
    }
    */


    std::for_each(key_pool_.begin(), key_pool_.end(), [&] (key_type n) {
	fullset getcomplete = request_inputs_generator_set();
	// Ensure that cache is warmed up only until it is nearly full
	if( (cache.space_used() + std::get<2>(getcomplete)) < cache_size) {
	    cache.set(n, std::get<1>(getcomplete), std::get<2>(getcomplete));
	}   
    });
    std::cout << "Now warm." << std::endl;
}


//header for workload_generator.cc

#include <chrono>
#include <vector>
#include <random>
#include <cmath>
#include <stdint.h>
#include <string>
#include <algorithm>
#include <iostream>
#include "cache.hh"
#include "evictor.hh" //for key_type

using fullset = std::tuple<key_type, Cache::val_type, Cache::size_type>;

class workload_generator
{
private:
    /* data */
    std::default_random_engine generator_;
    std::vector<key_type> key_pool_;
    std::vector<std::string> val_pool_;
    mutable std::string value_s_;
    enum data_type{key, value};

    std::string generate_a_string(int inputsize);
    int generate_length(data_type type);
    void fill_pool_key(int generatenumber);
    void fill_pool_val(int generatenumber);

    float set_number_ = 0.02;
    float del_number_ = 0.31;
    float get_number_ = 0.3111;

public:
    enum req_type{get, set, del};
    
    workload_generator(int poolsizes);
    ~workload_generator() = default;

    fullset request_inputs_generator_set();
    key_type request_inputs_generator_del();
    key_type request_inputs_generator_get();
    req_type case_generator();
    
    void warmup_cache(Cache& cache);
    
};

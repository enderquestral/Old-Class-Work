

#include <chrono>
//#include <stdlib.h>     /* srand, rand */
#include <vector>
#include <random>
#include <stdint.h>
//#pragma once 
using namespace std;
using data_t = float;



void update_coords(int iters, vector<data_t>& xs, vector<data_t>& ys, vector<data_t>& zs, vector<data_t>& vx, vector<data_t>& vy, vector<data_t>& vz);
vector<data_t> generate_random_list(int size, double bound, default_random_engine& generator);


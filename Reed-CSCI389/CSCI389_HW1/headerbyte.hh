


#include <chrono>
#include <vector>
#include <streambuf> //Mostly just for stringbuf?
#include <random>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdint.h>
#include <cassert>
#pragma once
using namespace std;

void init_buffer(int bufferSize, default_random_engine& generator, vector<int>& buffer);

// To build:
// g++-8 -Wall -Wextra -pedantic  --std=c++17 -g  -pthread mapreduce.cc  sum_nums.cc -o wc
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include "mapreduce.hh"
using namespace std;
using namespace MapReduce;
int global_counter = 0;

void map(const char* file_name) {
    FILE *fp = fopen(file_name, "r");
    assert(fp != NULL);
    char *line = NULL;
    size_t size = 0;
    while (getline(&line, &size, fp) != -1) {
        char *token, *dummy = line;
        while ((token = strsep(&dummy, " \t\n\r")) != NULL) {
            MR_Emit(token, "1");
        }
    }
    free(line);
    fclose(fp);
}
void reduce(const string& key, getter_t get_next, int partition_number) {
    int count = 0;
    string value;
    while ((value = get_next(key, partition_number)) != ""){
        count++;
        if (key != "")
        {
            global_counter += stoi(key);
        }
        
    }
    //global_counter += count;
}
int main(int argc, char *argv[]) {
    MR_Run(argc, argv, map, argc-1, reduce, 4, MR_DefaultHashPartition);
    std::cout << global_counter << std::endl;
}
// To build:
// g++-8 -Wall -Wextra -pedantic  --std=c++17 -g  -pthread mapreduce.cc  url_acc_freq.cc -o wc
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include "mapreduce.hh"
using namespace std;
using namespace MapReduce;

//Log example 1 from here: https://www.jafsoft.com/searchengines/log_sample.html 
//Log example 2 from here: https://www.satsig.net/logfile.htm

//We can assume that each url is surrounded by double quotes and followed by empty space
//We CANNOT assume there to only be one url per line
//We can assume assume that each url starts with http:// or https://
void map(const char* file_name) {
    FILE *fp = fopen(file_name, "r");
    assert(fp != NULL);
    char *line = NULL;
    size_t size = 0;

    while (getline(&line, &size, fp) != -1) {
        char *token, *dummy = line;
        while ((token = strsep(&dummy, " \t\n\r")) != NULL) {
            //Token is a URL surrounded by quotes
            if (strstr(token,"\"http") != NULL)  //Cool, you're looking at URL
            {
                MR_Emit(token, "1");
            }
            
            
        }
    }

    free(line);
    fclose(fp);
}
void reduce(const string& key, getter_t get_next, int partition_number) {
    int count = 0;
    string value;
    while ((value = get_next(key, partition_number)) != "")
        count++;
    std::cout << key << " " << count << std::endl;
}
int main(int argc, char *argv[]) {
    MR_Run(argc, argv, map, argc-1, reduce, 4, MR_DefaultHashPartition);
}
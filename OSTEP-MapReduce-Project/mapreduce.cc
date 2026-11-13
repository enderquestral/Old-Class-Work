#include <iostream>
#include <sys/sysinfo.h> //This complains in mac but is fiiiine on linux. Maybe need to use this?
#include <vector>
#include <algorithm>
#include <string>
#include <cassert>
#include <mutex>
#include <fstream>
#include <thread> // Need these for threads
#include "mapreduce.hh" //uses namespace MapReduce 
// data structure map seems to be included in std::

/*
Considerations: 
Thread Management. This part is fairly straightforward. You should create num_mappers mapping threads, and assign a file to each Map() invocation in some manner you think is best (e.g., Round Robin, Shortest-File-First, etc.). Which way might lead to best performance? You should also create num_reducers reducer threads at some point, to work on the map'd output.

Partitioning and Sorting. Your central data structure should be concurrent, allowing mappers to each put values into different partitions correctly and efficiently. Once the mappers have completed, a sorting phase should order the key/value-lists. Then, finally, each reducer thread should start calling the user-defined Reduce() function on the keys in sorted order per partition. You should think about what type of locking is needed throughout this process for correctness.

Memory Management. One last concern is memory management. The MR_Emit() function is passed a key/value pair; it is the responsibility of the MR library to make copies of each of these. Then, when the entire mapping and reduction is complete, it is the responsibility of the MR library to free everything.

*/


//Defined types: 
//using getter_t = std::function<const std::string(const std::string& key, int partition_number)>;
//using mapper_t = std::function<void(const char* filename)>;
//using reducer_t = std::function<void(const std::string& key, getter_t getter, int partition_number)>;
//using partitioner_t = std::function<unsigned long(const std::string& key, int num_partitions)>;
//your library will create some kind of internal data structure to pass keys and values from mappers to reducers

//store some data as global variables because there was no other way to pass them to some predefined functions.
//Can make our own custom Map and Reduce functs

//Make a struct of a vector of tuples for key-value pairs form mapper to reducer
//expect a global var or twol perhaps a global vector

//////////////////////////////////////////////////////////////////////////////
// TO DO LIST //
/*
1. Get rid of errors that come from porting from C, make it functioning c++
2. Get it working with wordcount (since we already have functions for wordcount)
3. Add threading to parallelize map and reduce
4. Make sure valgrind is a-okay with our work
5. Start looking at and implementing other tests other than wordcount. Make it more general/vague. 
*/

//////////////////////////////////////////////////////////////////////////////
// STRUCTS & GLOBAL OBJECTS//

struct mapped_object // A line of same characters, compressed into one character and the length
{
	int identifier = 0; //which reduce thread is handling this bunch of keys
    std::string key = ""; //key
	std::vector<std::string> values; //value, assume only one value

    bool operator!=(const mapped_object& other) const {
        return key != other.key;
    }
    bool operator==(const mapped_object* other) const {
        return key == other->key;
    }

};


std::vector<mapped_object> all_mapped_sections; //What map returns that we then split up to go into reduce

std::mutex mtx; //use for mtx.lock() and mtx.unlock()
std::mutex mtx2; //use for mtx.lock() and mtx.unlock()
std::mutex alpha_lock;

MapReduce::mapper_t globalMapper;
MapReduce::reducer_t globalReducer;
MapReduce::partitioner_t globalPartitioner;
int num_reducer_threads;

//////////////////////////////////////////////////////////////////////////////
// FUNCTIONS //

std::string find_value(const std::string& key, int partition_number){
    //Used for getter_t / get_next
    //return first value that corresponds with the key, then gets rid of it in the vector. If no results,return ""
	std::string desired_value = "";
	int map_index = 0;
	mapped_object new_mapped;
	
    for (auto map : all_mapped_sections) {
		if (map.key == key && map.identifier == partition_number) {
			if (map.values.size() == 0) {
				desired_value = "";
			} else {
				desired_value = map.values.front();
				map.values.erase(map.values.begin());
			}
			new_mapped.key = map.key;
			new_mapped.identifier = map.identifier;
			new_mapped.values = map.values;
            all_mapped_sections[map_index] = new_mapped;
			break;
		}
		map_index += 1;
	}
	
	return desired_value;
}


void MapReduce::MR_Emit(const std::string& key, const std::string& value){
    //create intermediate key-value pairs
    unsigned long partitionNum;
    if (globalPartitioner != NULL)
    {
		partitionNum = globalPartitioner(key, num_reducer_threads);//may need to make it a special num instread of 1?
    }
    else
    {
		partitionNum = MapReduce::MR_DefaultHashPartition(key, num_reducer_threads);
    }

	bool found_in_vector = false;
	mapped_object mapped_thing;
	
    alpha_lock.lock();
	int item_index = 0;
	for(auto mapped_item : all_mapped_sections) {
		if (mapped_item.key == key) {
			mapped_thing = mapped_item;
			found_in_vector = true;
			break;
		}
		item_index += 1;
	}
	
	if (found_in_vector) {
		auto alpha_iter = mapped_thing.values.begin();
		while (value > *alpha_iter) {
			alpha_iter += 1;
		}
		(mapped_thing.values).insert(alpha_iter, value);
		all_mapped_sections[item_index] = mapped_thing;
	} else {
		mapped_thing.identifier = partitionNum;
        mapped_thing.key = key;
        (mapped_thing.values).push_back(value);

		auto alpha_iter = all_mapped_sections.begin();
		if (all_mapped_sections.size() > 0) {
			while (alpha_iter != all_mapped_sections.end() && mapped_thing.key > alpha_iter->key) {
				alpha_iter += 1;
			}
		}
        all_mapped_sections.insert(alpha_iter, mapped_thing);
	}
	alpha_lock.unlock();
}

void reduce_wrapper(std::vector<std::string> keys, MapReduce::getter_t get_next, int partition_number){
    mtx2.lock();
    for (auto key: keys)
    {
        globalReducer(key, get_next, partition_number);
    }
    mtx2.unlock();
}

void MapReduce::MR_Run(int argc, char *argv[], mapper_t map, int num_mappers, reducer_t reduce, int num_reducers, partitioner_t partition){
    // effectively the main funct, where all stuff should go
    // creare specified numbers of mapping threads
    // splits up workload, and identifies it by key-value pair (segment of workload is value, identifier is key)
    // each one of the key-value pairs gets sent to a thread to be mapped

    if (argc == 1)
    {
        printf("Bad formatting. Please give at least one file.\n");
        exit(1);
    }

    //Once things get mapped, it gets sent back here and then it does a similar things with processed-mapped data and reduce threads
    //num_partitions == num reducer threads
    std::vector<std::thread> thread_pool_map;
    std::vector<std::thread> thread_pool_reduce;
    thread_pool_map.reserve(num_mappers);
    thread_pool_reduce.reserve(num_reducers);
    //Hopefully this'll work if we need to access these functions often.
    globalMapper = map;
    globalReducer = reduce;
    globalPartitioner = partition;
	num_reducer_threads = num_reducers;

    int numFiles = argc-1;
    std::vector<const char*> allFiles;
    for(int i=0;i<numFiles;i++)
	{
		allFiles.push_back(argv[i+1]);
	}

    mtx.lock();

    //Partition here? Somewhere?????
    //need to account for the possibility of multiple files w/ argc and argv

    for(int i = 0; i < num_mappers; i++)
    {
        auto file_name = allFiles[i];
        thread_pool_map.push_back(std::thread(std::bind(map, file_name))); //replace someData
    }
    
    for (int i = 0; i < num_mappers; i++) {
        thread_pool_map[i].join();//gotta join all the mapper threads here
    }

    std::vector<std::vector<std::string>> key_holder_vector;
    for (int i = 0; i < num_reducers; i++)
    {
        std::vector<std::string> key_holder; //one list for each partition, each list has a ton of keys
        key_holder_vector.push_back(key_holder);
    }
    
    for (auto mapped_thing : all_mapped_sections)
    {
        auto hold_id = mapped_thing.identifier; //we know which list this goes into thanks to the ID
        key_holder_vector[hold_id].push_back(mapped_thing.key);
    }

    for(int j = 0; j < num_reducers; j++)
    {   
        //reduce once for each key
        //Partition num gets assigned based on the key
        // Given a key, we can use MapReduce::MR_DefaultHashPartition(key, 1); to get the partition number.

        thread_pool_reduce.push_back(std::thread(std::bind(reduce_wrapper, key_holder_vector[j], find_value, j)));
    }
    
    for (int i = 0; i < num_reducers; i++) {
        thread_pool_reduce[i].join();//gotta join all the reducer threads here
    }
    mtx.unlock();
}

///////// The below may need to be edited, depending on what kind of job is running
//Adapted from the README
unsigned long MapReduce::MR_DefaultHashPartition(const std::string& key, int num_partitions){
	unsigned long hash = 5381;
	int c = 0;
    while (key[c] != '\0')
	{
        hash = hash * 33 + key[c];
		c += 1;
	}
    return hash % num_partitions;
}

# OSTEP-MapReduce-Project
Map Reduce Project written by Danny Riso and Hannah Hellerstien

## Map Reduce

In 2004, engineers at Google introduced a new paradigm for large-scale
parallel data processing known as MapReduce (see the original paper
[here](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf),
and make sure to look in the citations at the end). One key aspect of
MapReduce is that it makes programming such tasks on large-scale clusters easy
for developers; instead of worrying about how to manage parallelism, handle
machine crashes, and many other complexities common within clusters of
machines, the developer can instead just focus on writing little bits of code
(described below) and the infrastructure handles the rest.

In this project, we'll be building a simplified version of MapReduce for just
a single machine. While somewhat easier to build MapReduce for a single
machine, there are still numerous challenges, mostly in building the correct
concurrency support. Thus, we'll have to think a bit about how to build the
MapReduce implementation, and then build it to work efficiently and correctly.

There are three specific objectives to this assignment:

- To learn about the general nature of the MapReduce paradigm.
- To implement a correct and efficient MapReduce framework using threads and
  related functions.
- To gain more experience writing concurrent code.

## How to Run
- First, in this repo call 'make' or 'make all' to compile everything needed for this.
- Once that is done, decide what tests you want to call. There are 3 available: Wordcount, Link Access, and Sum-Numbers
    - To run wordcount, type './test_wordcount word-count1.txt' or './test_wordcount word-count1.txt word-count2.txt'  
    - To run link access, type './test_url_acc_freq log-example.txt' or './test_url_acc_freq log-example.txt log-example2.txt' 
    - To run sum ints, type './test_sumnums word-count1.txt' or './test_sumnums word-count1.txt word-count2.txt' 


### Background

To understand how to make progress on any project that involves concurrency,
we need to understand the basics of thread creation, mutual exclusion (with
locks), and signaling/waiting (with condition variables). These are described
in the following book chapters:

- [Intro to Threads](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf)
- [Threads API](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-api.pdf)
- [Locks](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks.pdf)
- [Using Locks](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-locks-usage.pdf)
- [Condition Variables](http://pages.cs.wisc.edu/~remzi/OSTEP/threads-cv.pdf)
.

### General Idea

Let's now get into the exact code we'll have to build. The MapReduce
infrastructure we will build supports the execution of user-defined `Map()`
and `Reduce()` functions.

As from the original paper: "`Map()`, written by the user, takes an input pair
and produces a set of intermediate key/value pairs. The MapReduce library
groups together all intermediate values associated with the same intermediate
key K and passes them to the `Reduce()` function."

"The `Reduce()` function, also written by the user, accepts an intermediate
key K and a set of values for that key. It merges together these values to
form a possibly smaller set of values; typically just zero or one output value
is produced per `Reduce()` invocation. The intermediate values are supplied to
the user's reduce function via an iterator."

A classic example, written here in pseudocode, shows how to count the number
of occurrences of each word in a set of documents:

```
map(String key, String value):
    // key: document name
    // value: document contents
    for each word w in value:
        EmitIntermediate(w, "1");

reduce(String key, Iterator values):
    // key: a word
    // values: a list of counts
    int result = 0;
    for each v in values:
        result += ParseInt(v);
    print key, result;
```

What's fascinating about MapReduce is that so many different kinds of relevant
computations can be mapped onto this framework. The original paper lists many
examples, including word counting (as above), a distributed grep, a URL
frequency access counters, a reverse web-link graph application, a term-vector
per host analysis, and others. 

What's also quite interesting is how easy it is to parallelize: many mappers
can be running at the same time, and later, many reducers can be running at
the same time. Users don't have to worry about how to parallelize their
application; rather, they just write `Map()` and `Reduce()` functions and the
infrastructure does the rest.

### Code Overview

We give here the
[`mapreduce.h`](https://github.com/remzi-arpacidusseau/ostep-projects/tree/master/concurrency-mapreduce/mapreduce.h)
header file that specifies exactly what we must build in our MapReduce library:

```
#ifndef __mapreduce_h__
#define __mapreduce_h__

// Different function pointer types used by MR
typedef char *(*Getter)(char *key, int partition_number);
typedef void (*Mapper)(char *file_name);
typedef void (*Reducer)(char *key, Getter get_func, int partition_number);
typedef unsigned long (*Partitioner)(char *key, int num_partitions);

// External functions: these are what you must define
void MR_Emit(char *key, char *value);

unsigned long MR_DefaultHashPartition(char *key, int num_partitions);

void MR_Run(int argc, char *argv[], 
	    Mapper map, int num_mappers, 
	    Reducer reduce, int num_reducers, 
	    Partitioner partition);

#endif // __mapreduce_h__
```

The most important function is `MR_Run`, which takes the command line
parameters of a given program, a pointer to a Map function (type `Mapper`,
called `map`), the number of mapper threads our library should create
(`num_mappers`), a pointer to a Reduce function (type `Reducer`, called
`reduce`), the number of reducers (`num_reducers`), and finally, a pointer to
a Partition function (`partition`, described below).

Thus, when a user is writing a MapReduce computation with our library, they
will implement a Map function, implement a Reduce function, possibly implement
a Partition function, and then call `MR_Run()`. The infrastructure will then
create threads as appropriate and run the computation.

One basic assumption is that the library will create `num_mappers` threads
(in a thread pool) that perform the map tasks. Another is that our library 
will create `num_reducers` threads to perform the reduction tasks. Finally,
our library will create some kind of internal data structure to pass
keys and values from mappers to reducers; more on this below.

### Considerations

Here are a few things to consider in our implementation:

- **Thread Management**. This part is fairly straightforward. Our should
    create `num_mappers` mapping threads, and assign a file to each `Map()`
    invocation in some manner we think is best (e.g., Round Robin,
    Shortest-File-First, etc.). Which way might lead to best performance?  We
    should also create `num_reducers` reducer threads at some point, to work
    on the map'd output.

- **Partitioning and Sorting**. Our central data structure should be
    concurrent, allowing mappers to each put values into different
    partitions correctly and efficiently. Once the mappers have completed, a
    sorting phase should order the key/value-lists. Then, finally, each
    reducer thread should start calling the user-defined `Reduce()` function
    on the keys in sorted order per partition. Our should think about what
    type of locking is needed throughout this process for correctness.

- **Memory Management**. One last concern is memory management. The
    `MR_Emit()` function is passed a key/value pair; it is the responsibility
    of the MR library to make copies of each of these. Then, when the entire
    mapping and reduction is complete, it is the responsibility of the MR
    library to free everything.




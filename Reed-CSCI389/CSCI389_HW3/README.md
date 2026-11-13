# cs389_hw3

I used the testing framework Catch2. I have 4 test cases: plain cache, cache integration, fifo, and lru.

Each "test" is a section, with test code found in `test_evictors.cc` and `test_cache.cc`. 

### Plain Cache
| test name     | description                                                          | status |
|---------------|----------------------------------------------------------------------|--------|
| insert + get  | can keys and values be inserted                                      | pass   |
| empty query   | uninserted items are not found                                       | pass   |
| basic delete  | delete removes items                                                 | pass   |
| reset         | reset removes all items                                              | pass   |
| duplicates    | duplicate entries overwrite eachtother                               | pass   |
| full cache    | a cache will fill up until it hits its capacity, then it wont accept | pass   |
| unsafe values | cache copies values passed to it                                     | pass   |

### Cache Integration
Note: I still consider these unit tests. They are not a test of the
evictor. Instead, they test whether the cache performs correctly when given a
evictor. 
| test name  | description                               | status |
|------------|-------------------------------------------|--------|
| basic      | cache can accept an evictor, and it works | pass   |
| duplicates | cache handles duplicate evictions         | pass   |
| robustness | robustness check on evictor integration   | pass   |
| scale      | scale check on evictor integration        | pass   |

### FIFO Evictor
| test name   | description                              | status |
|-------------|------------------------------------------|--------|
| basic       | evictor is stable, returns "" on empty   | pass   |
| duplicates  | evictor handles duplicate keys correctly | pass   |
| unsafe item | evictor handles temporary values         | pass   |

### LRU Evictor
| test name   | description                                 | status |
|-------------|---------------------------------------------|--------|
| basic       | evictor is stable, returns "" on empty      | pass   |
| juggle      | evictor will not reject recently given keys | pass   |
| unsafe item | evictor handles temporary values            | pass   |


Note: There are cache/evictor submissions after Monday. This is to reflect
updates made on the homework 2 repository, as that due date was extended to before
class on Wednesday.


## Arthur and Ian
First, I note that we see a malloc error, for use after free on the test of `cache_lib` included in the git-hub repository. This is after the "All tests passed! Fuck yeah!!" line. 

### Compilation Issues
There was no `#include <unordered_map>` which is a compile time failure. For the cache's I observed several problems. First: The LRU evictor won't compile. It has numerous syntax errors and bad return types. The README claims it was never tested. I don't plan to change that. Second: the `evictor.hh` file was modified. 

### Errors
First, on line 49 and 85 you have debug printouts included. These should not be there. An empty get should return a `nullptr`, instead an empty string. While tests are expected to be independent, many tests rely on asserting that an entry that shouldn't be there is `nullptr`. This interface error broke `empty query`, `basic delete` and `reset`. 
### Plain Cache
| test name     | status   |
|---------------|----------|
| insert + get  | pass     |
| empty query   | fail     |
| basic delete  | fail     |
| reset         | fail     |
| duplicates    | pass     |
| full cache    | fail     |
| unsafe values | SEGFAULT |
### Evictors:
	Note: linking was a pain, because the `evictor.hh` file was modified. 
### FIFO Evictor
| test name   | description                              | status |
|-------------|------------------------------------------|--------|
| basic       | evictor is stable, returns "" on empty   | pass   |
| duplicates  | evictor handles duplicate keys correctly | fail   |
| unsafe item | evictor handles temporary values         | pass   |

## Flaster and Strand
### Compilation Issues
There was a missing `Cache::~Cache(){}` in `cache.cc`, which was supposed to be called `cache_lib.cc`. You were also missing `const` in the Fifo header file. 

### Plain Cache
| test name     | status |
|---------------|--------|
| insert + get  | pass   |
| empty query   | pass   |
| basic delete  | pass   |
| reset         | pass   |
| duplicates    | fail   |
| full cache    | pass   |
| unsafe values | pass   |

### Fifo Evictor
The evictor does not return `""` on an empty evict. 
| test name   | description                              | status |
|-------------|------------------------------------------|--------|
| basic       | evictor is stable, returns "" on empty   | fail   |
| duplicates  | evictor handles duplicate keys correctly | pass   |
| unsafe item | evictor handles temporary values         | pass   |

## Hannah and Danny
### Compilation
I was happily surprised to find no issues with compiling my cache tests. `fifo_evictor.hh` and `lru_evictor.hh` was missing `#pragma once`. 
### Plain Cache
The the string copy in lines 78-82 in `cache_lib.cc` doesn't include the ending bit. I would encourage use of a simple memcopy, as the interface claims not to require a string (though it does). If copying a cstring is necessary, use strcpy. If handwriting code is necessary, try:

``` c++
uint32_t j(0);
do {
  copyavalue[j] = val[j];
} while (val[j++] != '\0');
```
This causes all tests that asses the value of a result to fail. The Cache never returns a valid string. 
| test name     | status |
|---------------|--------|
| insert + get  | fail   |
| empty query   | pass   |
| basic delete  | pass   |
| reset         | pass   |
| duplicates    | fail   |
| full cache    | fail   |
| unsafe values | fail   |

### FIFO Evictor
| test name   | description                              | status |
|-------------|------------------------------------------|--------|
| basic       | evictor is stable, returns "" on empty   | pass   |
| duplicates  | evictor handles duplicate keys correctly | pass   |
| unsafe item | evictor handles temporary values         | pass   |

### LRU Evictor
The `LRU_Evictor` does not return `""` on an empty `evict()`.
| test name   | description                                 | status |
|-------------|---------------------------------------------|--------|
| basic       | evictor is stable, returns "" on empty      | fail   |
| juggle      | evictor will not reject recently given keys | pass   |
| unsafe item | evictor handles temporary values            | pass   |

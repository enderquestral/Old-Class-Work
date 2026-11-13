#Priority was given to our test file, but having sanity checks helps.

CXX=g++-8 #clang++ ?
CXXFLAGS= -std=c++17 -Wall -Wextra -Werror -pedantic -O3
LIBS=-pthread


all: cache_server test_cache_lib test_cache_client simple_client baseline_client

test_cache_lib : test_cache_lib.o cache_lib.o lru_evictor.o fifo_evictor.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

cache_server: cache_server.o cache_lib.o lru_evictor.o fifo_evictor.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS) -lboost_program_options

test_cache_client: test_cache_client.o cache_client.o 
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

simple_client: simple_client.o workload_generator.o cache_client.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

baseline_client: baseline_client.o workload_generator.o cache_client.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

clean:
	-rm -rf *.o test_cache_lib test_cache_client cache_server simple_client baseline_client

test:
	./simple_client

base:
	./baseline_client 250000

valgrind:
	valgrind --leak-check=full --show-leak-kinds=all ./simple_client

debug:
	gdb ./simple_client

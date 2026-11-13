#Priority was given to our test file, but having sanity checks helps.

CXX=g++-8 #clang++ ?
CXXFLAGS= -std=c++17 -g -Wall -Wextra -Werror -pedantic -O0
LIBS=-pthread


all: cache_server test_cache_lib test_cache_client

test_cache_lib : test_cache_lib.o cache_lib.o lru_evictor.o fifo_evictor.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

cache_server: cache_server.o cache_lib.o lru_evictor.o fifo_evictor.o
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS) -lboost_program_options

test_cache_client: test_cache_client.o cache_client.o 
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

clean:
	-rm -rf *.o test_cache_lib test_cache_client cache_server

test:
	./test_cache_client
	echo "test_cache_client must be run manually against a running server"

valgrind:
	valgrind --leak-check=full --show-leak-kinds=all ./test_cache_lib
debug:
	gdb ./test_cache_client

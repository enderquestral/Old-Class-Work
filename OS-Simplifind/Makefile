CXX=g++-8
CXXFLAGS= -std=c++17 -g -Wall -Wextra -Werror -pedantic -pthread -O0
LIBS = -lstdc++fs

default: myfind

all: myfind 

myfind: myfind.cc
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LIBS)

clean:
	-rm -rf *.o myfind

test:
	./myfind foo.txt
	./myfind .

valgrind:
	valgrind ./myfind foo.txt
	valgrind ./myfind .

debug:
	gdb ./myfind
CXX=g++-8
CXXFLAGS= -std=c++17 -g -Wall -Wextra -Werror -pedantic -pthread -O0

default: test_wordcount

all: test_wordcount test_sumnums test_url_acc_freq

test_wordcount: mapreduce.cc wc.cc
	$(CXX) $(CXXFLAGS) -o $@ $^

test_sumnums: mapreduce.cc sum_nums.cc
	$(CXX) $(CXXFLAGS) -o $@ $^		

test_url_acc_freq: mapreduce.cc url_acc_freq.cc
	$(CXX) $(CXXFLAGS) -o $@ $^		

clean:
	-rm -rf *.o test_wordcount
	-rm -rf *.o sum_nums
	-rm -rf *.o url_acc_freq

test:
#	./mapreduce
	./test_wordcount word-count1.txt 
	./test_wordcount word-count1.txt word-count2.txt
	./test_sumnums sumbasicints.txt	
	./test_url_acc_freq log-example.txt

valgrind:
	#valgrind ./mapreduce
	valgrind ./test_wordcount word-count1.txt
	valgrind ./test_wordcount word-count1.txt word-count2.txt	
	valgrind ./test_sumnums sumbasicints.txt
	valgrind ./test_sumnums sumbasicints.txt sumlargerints.txt	
	valgrind ./test_url_acc_freq log-example.txt 

debug:
	gdb ./mapreduce
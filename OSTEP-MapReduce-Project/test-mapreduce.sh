#! /bin/bash

#Need to run multiple tests. At least one test from the README, at least one made on our own.

make all

echo "Testing word count over 1 file and 2"
./test_wordcount word-count1.txt
echo
./test_wordcount word-count2.txt
echo
./test_wordcount word-count1.txt word-count2.txt
echo
echo "Testing summing integers over 1 file and 2"
./test_sumnums sumbasicints.txt
echo
./test_sumnums sumlargerints.txt
echo
./test_sumnums sumbasicints.txt sumlargerints.txt

echo "Return code " $?

#custom test here?

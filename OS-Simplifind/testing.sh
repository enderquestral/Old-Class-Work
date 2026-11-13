# !/usr/bin/env bash
# Assumes a file $test_dir that contains folders. The name of these folders is
# the name of the test. Each folder contains a file "args" which is a string fed
# to both find commands. Then output is saved and compared.
​# I created and is unknown to you. You can create your own normal files and wild edge cases.
# I've only included the first five examples I'll tests. In my tests there'll be about two dozen more cases that are also unknown to you.
# There are some issues with comparing for exec (See: Exec-test-2, sym-link-exec-test) regarding the .DS_Store files which can change between calling this .sh. Maybe shouldn't call for Cat?

make all

for bin in find ./myfind
do
  echo Running tests with ${bin}
  mkdir ${bin}.out &> /dev/null
  rm ${bin}.out/*
  cp ./myfind tstdir/

  (cd tstdir; ${bin}; cd ..) &> ${bin}.out/no-args.out
  ${bin} tstdir &> ${bin}.out/one-arg.out
  ${bin} tstdir tstdir &> ${bin}.out/one-arg-dup.out
  ${bin} tstdir tstdir/dir1 &> ${bin}.out/two-args.out
  ${bin} . -print &> ${bin}.out/def-direc.txt
  ${bin} tstdir -mtime 0 &> ${bin}.out/mtime-test.out
  ${bin} tstdir -name foo &> ${bin}.out/name-test.out #gets a pattern
  ${bin} tstdir -type f &> ${bin}.out/file-type-test-1.out #Tries to search for files
  ${bin} tstdir -type f,d &> ${bin}.out/file-type-test-2.out #Tries to search for files and direcs
  ${bin} tstdir -name ba\* &> ${bin}.out/wildcard-test-1.out
  ${bin} tstdir -name ba\? &> ${bin}.out/wildcard-test-2.out #Should NOT include bark here
  ${bin} tstdir -name ba\[rz\] &> ${bin}.out/wildcard-test-3.out #Bat should not be included here
  ${bin} tstdir -type d -name bar &> ${bin}.out/direc-name-test-1.out #Find a directory of the name bar
  ${bin} tstdir -type f -name bar &> ${bin}.out/direc-name-test-2.out #Find a file of the name bar
  ${bin} tstdir -print &> ${bin}.out/print-test-1.out
  ${bin} tstdir -print -type f &> ${bin}.out/print-test-2.out #should have same output as print-test-1
  ${bin} tstdir -type f -print &> ${bin}.out/print-test-3.out 
  ${bin} tstdir -exec cat {} \; &> ${bin}.out/exec-test-1.out #Print the content of every File/directory
  ${bin} tstdir -type f -exec cat {} \; &> ${bin}.out/exec-test-2.out #Print the content of every File (not directory)
  ${bin} tstdir -type d -exec ls {} \; &> ${bin}.out/exec-test-3.out #Print the contents of ls-ing in every directory
  ${bin} -L tstdir  &> ${bin}.out/sym-link-test.out
  ${bin} -L tstdir -type f &> ${bin}.out/sym-link-type-test.out
  ${bin} -L tstdir -name ba\* &> ${bin}.out/sym-link-name-test.out
  ${bin} -L tstdir -type d -exec ls {} \; &> ${bin}.out/sym-link-exec-test.out
  ${bin} -L tstdir -mtime 0 &> ${bin}.out/sym-link-time-test.out

#These ones are supposed to produce errors or give nothing. Intentionally, even.
  ${bin} nodir &> ${bin}.out/nodir.out #What happens if we give a direct that isn't there?
  ${bin} tstdir -name cat &> ${bin}.out/no-file.out #Search for a file/direct that does not exist
  ${bin} tstdir -file &> ${bin}.out/inval-char-1.out #Start with a - or invalid character
  ${bin} tstdir file &> ${bin}.out/inval-char-2.out #Start with a - or invalid character 
  ${bin} tstdir -L &> ${bin}.out/l-after.out #Unknown predicate error
done

###############

echo "Comparing test outputs"

for out in find.out/*.out
do
  echo TESTING: $out ...
  diff $out ${bin}.out
done



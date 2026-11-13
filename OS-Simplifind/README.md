
# OS-Simplifind-Project
OS Simplifind Project written by Danny Riso and Hannah Hellerstien

## OS Simplifind


For this last project we will implement a simplified version of the UNIX command find. 
Our goal is to write a C++ program called `myfind` that efficiently scans a directory tree in a file system, searching for files that meet given criteria, and doing something with them (by default, just printing their names).

In particular, we need to support the following command line options:

`-name pattern` (including wildcards)
`-mtime n`
`-type t` (types are: b,c,f,d,l,s,p. Doors are not implemented. Multiple types are available by separating the letters by ,'s but NOT with a space)
`-exec command` (only the ; variant)
`-print`
`-L` (follow symbolic links)


## How to Run
Note: Please run this in a UNIX environment, compiling with g++-8
1. Compile using `make all`
2. To run test cases, please run with `testing.sh`
3. Compare the program outputs to the typical `find` outputs by myfind.out to find.out folders
4. If wished to run individual tests, please run `./myfind [flags with appropriate inputs]`
IMPORTANT NOTE: Please create your own symbolic link, as this seems to be computer specific. We recommend a `syn-test` in `tstdir` that links to `foo.txt`.


## Notes from the assignment

- Your output should be 100% identical to that of find on Linux for the supported options, including error messages and edge cases. I will use a testing script to verify this.
- find can take zero or more starting points. If zero are passed, . is assumed.
- If no -print OR -exec operations are passed as argument then -print is assumed (to test, simply try ./myfind .).
- The OS shell normally expands wildcards and special characters like * and ; on its own. To pass them explicitly to myfind, you'll need to use either quotation marks or backslash.
- Remember that a file matches only if all the concurrent options to find agree (are true), including a zero output from any -exec options. But you don't need to support any of find's logical operators such as -not.

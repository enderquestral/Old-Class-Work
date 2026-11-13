#pragma once

#include <iostream>
#include <sys/sysinfo.h> //This complains in mac but is fiiiine on linux. Maybe need to use this?
#include <sys/stat.h> // To get last write time of symlinks
#include <vector>
#include <string>
#include <stdlib.h>
#include <iterator>
#include <boost/algorithm/string.hpp> 
#include <filesystem> //recc'd by the assignment
#include <chrono> // for last_write_time calculations
#include <fnmatch.h> // Allows comparing wildcards in -name pattern
#include <functional>

namespace MyFind{

/*
-name pattern (including wildcards)
-mtime n (to simplify, I will only test with n=0, so don't bother with negatives or plus sign).
-type t
-exec command (only the ; variant).
-print
-L (follow symbolic links)
*/
struct predicate_holder 
{
    std::string flag = ""; //flag
	std::string value = ""; //If a flag needs other data

};


void name_find(const std::filesystem::path given_path, std::string pattern); //Given a vector of possible strings, including wildcards, find the name

void type_find(const std::filesystem::path given_path, std::string file_types, bool follow_symb_links);//File is of any of the following types: b,c,d,p,f,l,s,D   

void print_find(); //-print True; print the full file name on the standard output, followed by a newline

void exec_find(const std::filesystem::path given_path, std::string commands, bool follow_symb_links, bool is_final_pred); 
/*-exec command ;
Execute  command;  true  if 0 status is returned.  All following
arguments to find are taken to be arguments to the command until
an  argument  consisting of `;' is encountered.  The string `{}'
is replaced by the current file name being processed  everywhere
it occurs in the arguments to the command, not just in arguments
where it is alone, as in some versions of find.  Both  of  these
constructions might need to be escaped (with a `\') or quoted to
protect them from expansion by the shell. 
*/

void basic_find(bool is_following_symb_links,  std::vector<predicate_holder> predicates, std::vector<std::string> all_starting_direcs);

}

#include "myfind.hh"

/*
Needs to work like UNIX command find. (including erros messages)
https://shapeshed.com/unix-find/ 

In particular, you need to support the following command line options

'-name' pattern (including wildcards)
'-mtime' n (to simplify, I will only test with n=0, so don't bother with negatives or plus sign).
'-type' t
'-exec' command (only the ; variant).
'-print'
'-L' (follow symbolic links)

Note: -exec allows a command to be executed on files that are found
*/

//////////////////////////////////////////////////////////////////////////////
// STRUCTS & GLOBAL OBJECTS//

std::string initial_starting_direc = ".";
std::filesystem::path cur_path;
std::vector<std::filesystem::path > store_paths;
bool anything_in_vector = false;
bool is_following_symb_links = false;

//////////////////////////////////////////////////////////////////////////////
// FUNCTIONS //


void MyFind::name_find(const std::filesystem::path given_path, std::string pattern){ //-name. Given a vector of possible strings, including wildcards, find the name
    //Including wildcards: * [] ?
    // * = "there is some text here"
    // ? = "There is one character, any character, here"
    // [] = "In the file there is a character that matches at least one of the characters in the brackets"
    auto file_name = given_path.filename().string();
    pattern.erase(std::remove_if(pattern.begin(), pattern.end(), ::isspace), pattern.end());
	
    if (fnmatch(pattern.c_str(), file_name.c_str(), 0)) { // ! possibly?

        auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), given_path);
        if (holder_iter != store_paths.end())
        {
            store_paths.erase(holder_iter);
        }
	}
}


void MyFind::type_find(const std::filesystem::path given_path, std::string file_types, bool follow_symb_links){ //-type. File is of any of the following types: b,c,d,p,f,l,s,D 
    //Will likely return bool of "yes this fits the criteria"
    //Be sure to use std::filesystem::file_type for this, it'll be v handy. Or, is_block_file, is_character_file, is_regular_file
    
    //try an intersection of two vectors?
    std::vector<std::string> results; 
    boost::split(results, file_types, boost::is_any_of(",")); 
  
    for (size_t i = 0; i < results.size(); i++) 
    {

        results[i].erase(std::remove_if(results[i].begin(), results[i].end(), ::isspace), results[i].end());

        if (std::filesystem::is_block_file(given_path) && !results[i].compare("b"))
        { //b      block (buffered) special
            break;
        }
        else if (std::filesystem::is_character_file(given_path) && !results[i].compare("c"))
        { //c      character (unbuffered) specia
            break;
        }
        else if (std::filesystem::is_regular_file(given_path) && !results[i].compare("f"))
        { // f      regular file
            if (!std::filesystem::is_symlink(given_path)) 
            {
                break;
            }
            else if( std::filesystem::is_symlink(given_path) && follow_symb_links){
                break;
            }
            else if( std::filesystem::is_symlink(given_path) && !follow_symb_links){
				auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), given_path);
                if (holder_iter != store_paths.end())
                {
                    store_paths.erase(holder_iter);
                }
                break;
            }
        }
        else if(std::filesystem::is_directory(given_path) && !results[i].compare("d")){
            break;
        }
        else
        {
            if (std::filesystem::is_symlink(given_path) && !results[i].compare("l")){
                if (!follow_symb_links)
                {
                    break;
                }
                else{
                    break;
                }                
            }
            else if(std::filesystem::is_socket(given_path) && !results[i].compare("s")){
                break;
            }
            else if(std::filesystem::is_fifo(given_path) && !results[i].compare("p")){
                break;
            }
            else{ //Error/End-of-loop cases

                if (i+1 == results.size()){ //Nothing matches the type/type doesn't exist
                    auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), given_path);
                    if (holder_iter != store_paths.end())
                    {
                        store_paths.erase(holder_iter);
                    }
                }
            } 
        }
    }
}



void MyFind::print_find(){//-print True; print the full file name on the standard output, followed by a newline
    for (auto& s: store_paths) //W should be a string
    {
       std::cout << s.string() << '\n'; 
    }
	store_paths.clear();

} 

void MyFind::exec_find(const std::filesystem::path given_path, std::string commands, bool follow_symb_links, bool is_final_pred){
	// If this is the final predicate, carry out on all in the vector
	// Else, if exec rc != 0, remove the file from the vector
    
    if (!follow_symb_links)
    {
        auto path_name = given_path.string();
        auto file_name = given_path.filename().string();
        
        std::string brackets = "{}";
        size_t file_insert_pos = commands.find(brackets);
        while (file_insert_pos != std::string::npos) {
            commands.replace(file_insert_pos, brackets.size(), given_path.string());
            file_insert_pos = commands.find(brackets, file_insert_pos + given_path.string().size());
        }

        if (!is_final_pred)
        {
            if (system(commands.c_str()) != 0)
            {
                auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), given_path);
                if (holder_iter != store_paths.end())
                {
                    store_paths.erase(holder_iter);
                }
            }
        }
        else
        {
			system(commands.c_str()); //Might need to print this out? Or not?
        }
    }
    else //we are following symlinks
    {
        auto path_name = given_path.string();
        auto file_name = given_path.filename().string();

        std::string brackets = "{}";
        size_t file_insert_pos = commands.find(brackets);
        while (file_insert_pos != std::string::npos) {
            commands.replace(file_insert_pos, brackets.size(), given_path.string());
            file_insert_pos = commands.find(brackets, file_insert_pos + given_path.string().size());
        }
        if (std::filesystem::is_symlink(given_path))
        {
            auto target_path = std::filesystem::read_symlink(given_path);
            size_t file_insert_pos = commands.find(path_name); //could be file_name?

            while (file_insert_pos != std::string::npos) {
                commands.replace(file_insert_pos, brackets.size(), target_path.string());
                file_insert_pos = commands.find(brackets, file_insert_pos + target_path.string().size());
            } 
        }
        

        if (!is_final_pred)
        {
            if (!system(commands.c_str()) == 0)
            {
                //std::cout << file_name << std::endl;
                //add to vector
            
                auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), given_path);
                if (holder_iter != store_paths.end())
                {
                    store_paths.erase(holder_iter);
                }
            }
        }
        else
        {
            system(commands.c_str()); //Might need to print this out? Or not?
        }
    }
}


void MyFind::basic_find(bool is_following_symb_links, std::vector<MyFind::predicate_holder> predicates, std::vector<std::string> all_starting_direcs){
    //Make a struct to pass into basic find for the flags
    if (all_starting_direcs.size()==0) {
        all_starting_direcs.push_back(".");
    }
    
    for (auto& w: all_starting_direcs) //W should be a string
    {
        if (std::filesystem::exists(w))
        {
            store_paths.push_back(w); 
            for(auto& q: std::filesystem::recursive_directory_iterator(w)){
                store_paths.push_back(q.path()); //To init vector with all possible files/direcs from cur-direc
            }
            std::vector<std::filesystem::path> holder_for_paths = store_paths;
            
            //for all files ouside of current directory.
            for(auto& p: holder_for_paths){
                //p is each separate entry in directory	
                if (predicates.size() !=0 )
                {
                    for (size_t o = 0; o < predicates.size(); o++) {
                        auto pred = predicates.at(o);
                        if (!pred.flag.compare("print") ) {
                            if (!pred.value.compare("print"))
                            {
                                break;
                            }
                            else
                            {
                                if (!pred.value.compare("!"))
                                {
                                    std::cerr << "find: expected an expression after '!'" << '\n';
                                }
                                else
                                {
                                    std::cerr << "find: paths must precede expression:'"<< pred.value  << "'" << '\n';
                                }
                                return;
                            }
                        }
                        else if (!pred.flag.compare("mtime") ) {
                            auto n = std::stoi(pred.value);
                            if (n == 0) {
                                n = 1;
                            }
                            if (std::filesystem::is_symlink(p) && !is_following_symb_links) {
                                //This works as find intends, even without the -L. Hurray. Thank you Danny.
                                struct stat buffer;
                                int status = lstat(p.string().c_str(), &buffer);
                                // !!!!!!!!!!!!!!!!!!!!!
                                // This error message probably isn't right.
                                // It's in here now so status doesn't get an "unused variable" warning.
                                // Maybe we can see if there's a matching find error code later?
                                if (status != 0) {
                                    std::cerr << "Symlink path couldn't be read." << std::endl;
                                }
                                int write_time = buffer.st_mtime;
                                auto now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());

                                int seconds_between = now - write_time;
                                int hours_between = seconds_between / 3600;
                                if (hours_between >= n * 24) {
                                    auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), p);
                                    if (holder_iter != store_paths.end())
                                    {
                                        store_paths.erase(holder_iter);
                                    }
                                }
                            } 
                            else {
                                auto last_write = std::filesystem::last_write_time(p);
                                auto current_time = std::chrono::system_clock::now();
                                auto time_between = current_time - last_write;
                                auto hours_since_edited = std::chrono::duration_cast<std::chrono::hours>(time_between).count();
                                if (hours_since_edited >= n * 24) {
                                    auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), p);
                                    if (holder_iter != store_paths.end())
                                    {
                                        store_paths.erase(holder_iter);
                                    }
                                }
                            }
                        }
                        else if (!pred.flag.compare("name") ) {
                            MyFind::name_find(p, pred.value);
                        }
                        else if (!pred.flag.compare("type") ) {
                            MyFind::type_find(p, pred.value, is_following_symb_links);
                        }
                        else if (!pred.flag.compare("exec") ) {
                            if (o == predicates.size()-1)
                            {
                                if (std::find(store_paths.begin(), store_paths.end(), p) != store_paths.end()) {
                                    MyFind::exec_find(p, pred.value, is_following_symb_links, true);
                                    auto holder_iter =  std::find(store_paths.begin(), store_paths.end(), p);
                                    if (holder_iter != store_paths.end())
                                    {
                                        store_paths.erase(holder_iter);
                                    }
                                }
                            }
                            else
                            {
                                MyFind::exec_find(p, pred.value, is_following_symb_links, false);
                            }
                            
                        }
                        else //Had predicate flag that isn't allowed
                        {
                            std::cerr << "find: unknown predicate `-"<< pred.flag <<"'" << '\n';
                            return;
                        }
                    } 
                }
            }
            MyFind::print_find();
        }
        else
        {
            std::cerr << "find: ‘"<< w << "’: No such file or directory" << '\n';
        }
    }	
}


// find where-to-look criteria action
// Most of the time, the first input after find will be the starting search directory. But not always. It could be -L.
int main(int argc, char const *argv[])
{
    //Keep on looking through commands in the input line until we get one that starts with a -, (, or an !

    std::vector<std::string> all_starting_direcs;
    std::vector<MyFind::predicate_holder> predicates;
	std::string rest_of_command_line;
    
	if (argc == 1) 
    {
        MyFind::basic_find(false, predicates, all_starting_direcs);
    }
    else
    {
        if (strcmp(argv[1], "-L") == 0) {
            for (int i = 2; i < argc; i++) {
                rest_of_command_line += argv[i];
                rest_of_command_line += " ";
            }
            is_following_symb_links = true;
        }
        else{
            for (int i = 1; i < argc; i++) {
                rest_of_command_line += argv[i];
                rest_of_command_line += " ";
            }
            is_following_symb_links = false;
        }
        std::vector <std::string> tokens;
        std::stringstream check1(rest_of_command_line);
        std::string intermediate; 
        while(getline(check1, intermediate, '-')) 
        { 
            tokens.push_back(intermediate); 
        } //Tokens is now an array split up by dashes

        auto starting_direcs = tokens[0];
        auto curr_direct = starting_direcs.substr(0, starting_direcs.find(' ')); //If there isn't a space, gives whole starting direc string, else we're right to split it up
        auto holdspot = starting_direcs.find(' ')+1;

        while (curr_direct != "")
        {
            all_starting_direcs.push_back(curr_direct);
            curr_direct = starting_direcs.substr(holdspot, starting_direcs.find(' ', holdspot) - holdspot);
            holdspot =  starting_direcs.find(' ', holdspot) +1;
        }

        for(size_t i = 1; i < tokens.size(); i++) { //Split up by first space to get flag and value
            auto s = tokens[i];
            s = s.substr(0,s.size()-1);
            auto first_token = s.substr(0, s.find(' '));
            auto second_token = s.substr(s.find(' ')+1, s.size()); //size or len
            MyFind::predicate_holder temp_holder;
            temp_holder.flag = first_token;
            temp_holder.value = second_token;
            predicates.push_back(temp_holder);
        }
        MyFind::basic_find(is_following_symb_links,  predicates, all_starting_direcs);

    }
	
    return 0;
}
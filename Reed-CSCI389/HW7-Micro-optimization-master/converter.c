/*
 * Trivial implementation of converter function.
 * You may override this file or create your own.
 */
#include "converter.h"

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>


//#define getnumber(line, number)((*number<<1) + (*number << 3) + (*line++) - 48)//48 == '0'

/*void getnumber(char* line, quote_t* number){
  *number = ((*number<<1) + (*number << 3) + (*line++) - 48);//48 == '0'
}

quote_t valuetable[] = {0,1,2,3,4,5,6,7,8,9};
*/
// use unordered map?
// assume that the string read are all numerical, and thus don’t need to check for the string’s content
// for each is slower than for....


//Faster version

void convert_all(unsigned nlines, char *lines[], quote_t nums[])
{
  quote_t currentnumber;  
  char* currentline = lines[0];
  for (unsigned i = 0; i < nlines; i++) {
    currentnumber = (*currentline++) - 48;
    while (*currentline) 
    {
      currentnumber = ((currentnumber<<1) + (currentnumber << 3) + (*currentline++) - 48); //48 == '0'
    }
    currentline++; 
    *nums++ = currentnumber;
  }

}



//Naive version &
//Helper function, used for testing
/*
quote_t faster_atoi(char* currentline){
  quote_t currentnumber = 0; //Number to submit
    while (*currentline)
    {
      currentnumber = (currentnumber*10) + (*currentline++ - '0'); //shift number over to the left once, then use acii values to add next character
    }
  return currentnumber;
}

void convert_all(unsigned nlines, char *lines[], quote_t nums[]){
  for (unsigned i = 0; i < nlines; i++) {
    nums[i] = faster_atoi(lines[i]);
  }
}
*/

//Orig version
/*
void convert_all(unsigned nlines, char *lines[], quote_t nums[]){
  for (unsigned i = 0; i < nlines; i++) {
    nums[i] = atoi(lines[i]);
  }
  
}
*/

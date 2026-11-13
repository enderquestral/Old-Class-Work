# HW7-Micro-optimization
Written by Hannah Hellerstein
(Thank you to Casey Harris and Maxx Curtis for letting me bounce ideas off of them)
NOTE: Maxx and I both independently tried to valgrind the code, and it seemed to lose a TON of data. We suspect it was something in the driver.c code we were given.
NOTE: This was tested on a 2.3 GHz Dual-Core Intel Core i5, 8GB Memory MacBook Pro. I tried to use a Ubnutu VM for this, but it seemed more unreliable than the regular mac OS for some reason.

To build, simply run: g++ -O3 -std=c99 -march=native -o driver -Werror -Wall -Wextra -pedantic *.c

To test, run: ./driver quotes.txt 1000. (Fewer than  about a 1000 iterations can be noisy.) On my computer, this default implementation yields a best run time of 0.06396s on an Intel E5-2695v3 CPU and 0.0525s on an AMD 1950X, using g++-8.


### Part 1: Naive implementation (2 pt.)
The current implementation of convert_all() simply uses the standard C library atoi() function, which is always a good starting point, because standard library functions are well-debugged and documented. Your first task it to replace this call with your own implementation of the string conversion, as simple and readable as possible.

Measure the performance of your implementation, describe it in the README, and explain the performance difference you got from the atoi() version. You will get 1 point for a correct implementation and 1 point for a correct and complete performance explanation.


For simple atoi():
Best run time overall: 0.054021s

For handwritten atoi replacement (seen below):
Best run time overall: 0.008899s


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

  
  #### So, what happened?
Basically, from what I could tell from my research... the c library verison of atoi is not very well implemented. Since our task for this part of the assignment was to effectively recreate the atoi, I did just that. 
I knew that for a given line, I'd have to go character by character, turning them into numbers. This seemed to be done by taking a given number, times-ing it by 10 to create space for the next digit, getting the ascii value of the next character (which ranged from 0-9), and subtracting the ascii value of 0 to get the remainder, which is the next digit to be added. The return number is the one that is to be added to nums, and that finishes it. the *currentline++ seems to move us through the while loop on its own, so that's helpful. I was surprised that we didn't need to account for the '/0' character at the end of the given line input, but I guess not? Trying to do so caused segfaulting errors.


### Part 2: Optimized implementation (3+ pts).


I will compile and compare all of your implementations on my Linux host with gcc v. 8  (note that performance differences on a Mac will not necessarily translate to Linux).

Best run time overall: 0.005911s


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

  #### So, what changed?
Lots of things!
First off, I decided that making a helper function to call on every line, was likely not very efficient. So, I took some of the basic logic from the helper function, and placed it directly into the function itself. I attempted to do some inlining with the assignmeng within the inner while loop, but found no noticible difference.
Secondly, I tried some strentgh reduction. currentnumber*10 takes far longer than (currentnumber<<1) + (currentnumber << 3), which achieves the same affect of shifting the number over by one digit. In that same line I just subtracted bt 48 instead of the character of 0 since it would be the same affect and the conversion may take some time. Similarly, I created currentlline and currentnumber outside of the while loops, so they wouldn't have to be recreated all the time, just reassigned.
I tried to do loop unrolling in the inner while loop, believing it needed to be sped up, but the attempt ended in a failure: I didn't want to assign space/spend time checking for the length of a given line, and though I believed inlining would help I seemingly wasn't able to create a 'getnumber' function that affected the time noticibly. 

What was REALLY bizzare was running the code on the Ubnutu VM vs my Macbook proper. What was faster on one was markedly slower on the other, with the VM seemingly having stranger logic to that regard (what should be clear optimization in one respect like strength reduction made it slower on the VM for instance.)

GOAL OF THE CODE
This code here is HW0 of Computer Systerms 389. The goal: To understand, translate, and improve upon code performance.

-----------------------------------

Run this code for multiple object counts (say from 2^8 to 2^24 in powers of two). For a small number of objects, you'll need to run for many iterations (turns) to get a statistically stable measurement. For larger objects, many turns would take too long, and may not be necessary. But you'll probably still see some variation from run to run. Once you decide on good choices for the number of iterations, run the benchmark for all these sizes and collect the results. You may have to repeat a few runs and pick just one of those performance numbers such as average, minimum, median, etc. 

a. Explain in your README.md file how many iterations you picked at different sizes and why. There is no single correct answer here, I just want to see your reasoning. 
How I went about choosing iterations and object counts was through a bit of a brute force method. I decided to start my object count (as was suggested in the assignment) at 2^8, as if slowdown happens at a lower number than that then that would imply to me we have more problems than just this section of code. I then establlished that our otuer object counts would be 2^10, 2^11, 2^12, ... , 2^24 as I felt that it would provide a good spread of sizes, leaning towards the heavier end (surprisingly I only first saw real notable slowdown at 2^18, after which it got bad).
I then made a update_locations_helper2.py file that contained a list of iterations: [-1,1,10,100, 250, 500, 750, 1000, 2500, 5000, 7500, 8000, 9000, 10000]. This list was chosen as I felt that going up by decimal made sense, though from 100 to 1000 and 1000 to 10000 I could see some slowdown easily falling through in that difference, and by the end with higher object counts I somewhat went off script and started decreasing by lesser amounts manually. The -1 was there for my own curiosity, as I wanted to see how the system would react to somehow being fed negative turns (I would have added 0 as well, but the formula used in the code would have cause a DivideByZero error). Had I more time I likely would have played around more with negative inputs, float inputs, and more. 
Since higher object counts required fewer iterations to get something stable in a reasonable amount of time, after counciling with a friend (Maxx) I decided that each ordersize higher would mean dropping off the greatest value currently in iterations.
I then ran each objectcount-iterationnumber duo 10 times to get a spread of mean times. 

b. Explain how you picked a single number from repeated measurements and justify it. There is no single correct answer here either. 
After gathering all the numbers (seen in NotesFromPythonResults.md) I had to basically arbitrarily choose an appropriate iteration time. Since I ran each pairing 10 times, I just picked the outcome that seemed to be the closest of the mean running times presented (with a perhaps slight bias to lean towards the larger end of the scale). With that in mind, I got:

256 at 10000: 0.1605099417968603
512 at 9000: 0.15815279969623297 
1025 at 8000: 0.3200545768292679
2048 at 7500: 0.185152245182251
4096 at 5000: 0.2032384029785117 
8192 at 2500: 0.22719521669922746 
16384 at 2500: 0.2338650065429659 
32768 at 1000: 0.31573136294554827
65536 at 750: 0.1832900503540013
131072 at 500: 0.313263554046622
262144 at 250: 0.313838821350095 
524288 at 200: 0.26968447659492417
1048576 at 150: 0.27484881125767907
2097152 at 100: 0.272801874871254
4194304 at 50: 0.31795485583305594
8388608 at 25:0.32714554324150474
16777215 at 10:0.3510530949683


c. Plot a line graph of mean update time per coordinate as a function of total no. of objects (first parameter). You can use Excel or other GUIs, but it's best to stay in the Linux environment. I recommend learning how to use the "gnuplot" tool, which is both powerful and relatively straightforward, especially with text inputs.

[Please see pythontest.png]


--------------------------------
PART 2:
Note: I set data_t initially to float in this run.
[For the combined graph please see combinedtest.png]

--------------------------------
PART 3:
Observation time!

After running each doubling 10 times with each of the data types, from what I could tell there wasn't much a notable difference in running time. However, there was a difference in running time: int8_t <= int16_t <= int32_t <= int64_t < float < double. I suspect that this was because the int-types are signed, and also have a lower variance due to the fact that their numbers are restricted with number of bits. In contrast, floats and doubles could both be unsigned, meaning there is a higher range of possibilities to calculate/generate. I made two(sing gnuplot could only handle 3 files) graphs comparing the various CPP iterations, and by the end double seems to take longer. If you want to see graphical representation of how the values compare, please see CPPcomparison1.png and CPPcomparison2.png (Note: this was before I used -O3 in my compile time, so all versions should be notably slower, though in my experimentation the end observation stayed the same. )

---------------------------------
PART 4:
Figure out and describe a way to measure how much memory each of your benchmarks uses while running with 2^20 objects (can be approximate). Compare and contrast the performance and memory consumption of both versions.
Running 1048576 objects at 150 iterations for both the python and the c++ (c++ is running with data_t = float). 
Calling /usr/bin/time -v for both... 
Python:
	Command being timed: "python3 update_locations.py 1048576 150"
	User time (seconds): 26.27
	System time (seconds): 0.05
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:26.35
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 211440
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 51114
	Voluntary context switches: 16
	Involuntary context switches: 167
	Swaps: 0
	File system inputs: 24
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0

C++:
	Command being timed: "./upd8-loc-cpp 1048576 150"
	User time (seconds): 0.41
	System time (seconds): 0.02
	Percent of CPU this job got: 98%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.44
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 29580
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 12266
	Voluntary context switches: 7
	Involuntary context switches: 38
	Swaps: 0
	File system inputs: 0
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0


As far as I can tell, 'performance' refers to means sheer speed of the code (user time and system time, perhaps while considering elapsed time) while "memory consumption" means the maximum resident set size.
When it came to memory consumption, C++ took a bit over one tenth of the memory of the Python code, even when semi-optimized (changing the vectors to C-arrays could have made it a bit faster apparently). 
As for performance, the C++ code ran OBSURDLY fast in comparison to the Python. While the python took around 26 seconds user-time to run [1048576,150 ], the C++ didn't even take half a second. Interestingly enough, the system time of the C++ was oly a bit over twise as fast as the system time for the Python. 

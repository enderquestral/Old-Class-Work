#include "headerbyte.hh"
//I've been warned that this is impossible to do accurately, so... we shall see. 
//Wanted to do C arrays, but breaks aftter 2^22
const int BUFFER_POWER_MIN = 10; //1024;
const int BUFFER_POWER_MAX = 26; //67108864;
int TESTING_SIZE =  1000; //Should take around 4k bytes from cache, which should be fine?

void init_buffer(int bufferSize, default_random_engine& generator, vector<int>& buffer){
    //init with random characters
    generator();
    uniform_int_distribution<> distribution(0, bufferSize-1);
    for (int i = 0; i < bufferSize-1; i++)
    {        
        
        buffer.push_back(i); //Should keep things contiguous?
    }
    for (int j = 0; j < bufferSize-1; j++)
    {
        int k =j + distribution(generator) % (bufferSize -j);
        while (k == j)
        {
            k =j + distribution(generator) % (bufferSize -j);
        }
        
        swap(buffer[j], buffer[k]);
    }
    //random_shuffle(buffer.begin(), buffer.end());
    //shuffle(buffer.begin(), buffer.end(), generator()); //Initialize then make things random
    //shuffle an array manually takes one for loop

    //The buffer is being changed here
}

int main(){
    //Code should iterate through all the sizes

    //Init an array of chars as a char is a perfect byte in this context

    //default_random_engine generator; //Assuming we don't seed this thing
    cout <<"# Bytes:" <<  "\t" << "Time of one byte (nanoseconds):" << "\t " << "Useless printout: \n";
    //For first 100 times at a given buffer size, pull a random index so its forced to use a random size. not timed.
    //THEN we start timing, try accessing another random point (determined before start), time it, print that. 
    vector<int> buffer;
    default_random_engine generator; //Assuming we don't seed this thing
    for (int i = BUFFER_POWER_MIN; i <= BUFFER_POWER_MAX; i++)
    {   
        const int bufferSize = pow(2.0, double(i));
       
        init_buffer(bufferSize, generator, buffer);
        uniform_int_distribution<> byteDistribution(0, bufferSize-1);
        //then, access random iterations for enough time that the computer puts the buffer in L1 category
        int sumint = 0;
        int randomByte = 0;
        volatile int uselessvariable = 0;
        //Trying to put things into L1 here. I COULD just effectively copy the same logic used below, with the timed section and get rid of some ints... but I liked the numbers I got from this system better.
        for (int32_t j = 0; j < TESTING_SIZE; j++) //Caches work in sections of 64 bytes, so should access at least 1 out of every 64 bytes in fector
        {
            randomByte = byteDistribution(generator);
            //Read a byte
            uselessvariable = buffer[randomByte]; //Time how long it takes to get buffer access here?
            sumint += uselessvariable; 
            //volatile doesn't nessicarilly keep the thing
            //How to read a byte and assure it's not in L1? This is an L2 issue needed to be figured out. 
            // try to infer size of cache. 
            //-O3 compilier would get rid of variable we don't use, so we need to use it in a way that doesn't affect timing
            //Try using volatile for a variable so compiler wont get rid of it... but it can't be put in registers.
        }
        double meantime = 0.0; 

        int randomByteInt=0;
        chrono::time_point start = chrono::high_resolution_clock::now(); //start timing 
        
        for (int32_t k = 0; k < TESTING_SIZE; k++)
        {
            //Writing might be taking longer, but since we init the buffer with indecides into itself and shifted them, we should be getting random things.
            randomByteInt = buffer[randomByteInt];
        }
        
        chrono::time_point finish = chrono::high_resolution_clock::now(); //end timing
        meantime = chrono::duration_cast<chrono::microseconds>(finish - start).count(); 
        meantime *= 1000; //gotta make it nanoseconds
        meantime /= TESTING_SIZE;
        cout << bufferSize << "\t" << meantime << "\t"<<  randomByteInt << "\t" <<'\n';  //printing out the randomByteInt so the optimizer doesn't toss it.
        buffer.clear();
        TESTING_SIZE = TESTING_SIZE * 2;
    }
    //Add a control for outliers by taking the mean when graphing by running 10 times. 
    return 0;
} 
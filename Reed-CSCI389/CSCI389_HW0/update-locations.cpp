#include <iostream>
#include <cassert>
#include "upcate-locations.hh"
//FOR PART 3:
//Define data type, change it when you need
//remember to use -0fast for compiling!

//////////////

vector<data_t> generate_random_list(int size, double bound, default_random_engine& generator){
    vector<data_t> givenlist;
    //We must pass a generator address as we need to STEP the same generator with each call to this function.
    generator();
    uniform_real_distribution<> distribution((-1* bound), nextafter(bound, __DBL_MAX__));
    for (int i = 0; i < size; i++){
        data_t newitem = distribution(generator);
        givenlist.push_back(newitem);
    }
    

    return givenlist;
}

void update_coords(int iters, vector<data_t>& xs, vector<data_t>& ys, vector<data_t>& zs, vector<data_t>& vx, vector<data_t>& vy, vector<data_t>& vz){
    for (int k = 0; k < iters; k++)
    {
        for (long unsigned int i = 0; i < xs.size(); i++){ //May not edit proper things?
            xs[i] = xs[i] + vx[i];
            ys[i] = ys[i] + vy[i];
            zs[i] = zs[i] + vz[i];
        }
    }
}

int main(int argc, char* argv[]){
    if (argc != 3)
    {
        cout << "Required arguments: vector_length(N) and iterations_num(M)" <<'\n';
        exit(-1);
    }
    int size = stoi(argv[1]);
    int iters = stoi(argv[2]);
    default_random_engine generator (size);
    vector<data_t> xs = generate_random_list(size, 1000.,generator); //Could theoretically use c arrays to make this faster but we don't care rn
    vector<data_t> ys = generate_random_list(size, 1000.,generator);
    vector<data_t> zs = generate_random_list(size, 1000.,generator);
    vector<data_t> vx = generate_random_list(size, 1.,generator);
    vector<data_t> vy = generate_random_list(size, 1.,generator);
    vector<data_t> vz = generate_random_list(size, 1.,generator);

    chrono::time_point start = chrono::high_resolution_clock::now(); //start timing
    update_coords(iters, xs, ys, zs, vx, vy, vz); //I had the for loop inside update_coords at python timeit only creates scope once... though in practice it doesn't seem to matter at all.
    chrono::time_point finish = chrono::high_resolution_clock::now(); //end timing
    //auto chksum = accumulate(xs.begin(), xs.end(), 0.0) + accumulate(ys.begin(), ys.end(), 0.0) + accumulate(zs.begin(), zs.end(), 0.0); //Accumulate to sum all values in a vector.
    //Need to use 0.0 to make sure accumulate outputs a double    
    double meantime = chrono::duration_cast<chrono::microseconds>(finish - start).count(); //output is IN microseconds w/ highest tick time
    cout <<  meantime / (size*iters) << '\n';
    //cout << "Mean time per coordinate: " << meantime / (size*iters) << "μs \n";
    //cout << "Final checksum is: " << chksum << "\n"; 
    exit(0);
}


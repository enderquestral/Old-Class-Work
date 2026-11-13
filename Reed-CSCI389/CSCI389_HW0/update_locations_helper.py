import random, sys, timeit
sizes =  []
#iterations_set = [-1,1,10, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
runningnumber = 10

###############
# Create a list of 'size' floating point numbers in the range [-bound, bound]
def generate_random_list(size, bound):
    return [random.uniform(-bound, bound) for i in range(size)]

###############
# Update position by velocity, one time-step
def update_coords(xs, ys, zs, vx, vy, vz):
    for i in range(len(xs)):
        xs[i] = xs[i] + vx[i]
        ys[i] = ys[i] + vy[i]
        zs[i] = zs[i] + vz[i]

############ Reassigns things:
def reassignThings(objectsize, itersize):
    #Change size and iters
    size = objectsize
    iters = itersize
    random.seed(size)
    xs = generate_random_list(size, 1000.)
    ys = generate_random_list(size, 1000.)
    zs = generate_random_list(size, 1000.)
    vx = generate_random_list(size, 1.)
    vy = generate_random_list(size, 1.)
    vz = generate_random_list(size, 1.)
    #FIX THE BELOW BIT
    t = timeit.timeit(stmt =  '''
size = objectsize
iters = itersize
random.seed(size)
xs = generate_random_list(size, 1000.)
ys = generate_random_list(size, 1000.)
zs = generate_random_list(size, 1000.)
vx = generate_random_list(size, 1.)
vy = generate_random_list(size, 1.)
vz = generate_random_list(size, 1.)
update_coords(xs, ys, zs, vx, vy, vz)''',
        setup = "from __main__ import update_coords",
        number = iters)
    chksum = sum(xs) + sum(ys) + sum(zs)
    #print("Mean time per coordinate: " + str(1000000 * t / (size * iters)) + "μs")
    return (1000000 * t / (size * iters))

def TestInGroups(objectsizelist):
    #Make sure to reduce each thing by 1 or 2 sizes
    print("Calculating mean runtimes for " + str(runningnumber) + " different sizes at " + str(len(iterations_set)) + "different iteration set." )
    removelastnumbers = 0
    for j in objectsizelist:
        print("The times for " + str(j) + " Start here! \n" )
        for i in range(0, len(iterations_set)-removelastnumbers):
            print("The times for " + str(j) + " at size " + str(iterations_set[i]) + ":")
            givenvalue = iterations_set[i]
            for k in range(0, runningnumber):
                holdvalue =  reassignThings(j, givenvalue)
                print(holdvalue)
                
        removelastnumbers +=1

def testOnePair(objectsize, iterationsize):
    print("Calculating mean runtimes for " + str(runningnumber) + " different sizes at iteration size " + str(iterationsize) + " with object size " + str(objectsize) )
    for i in range(runningnumber):
        print(reassignThings(objectsize, iterationsize))
    print('\n')
    
import timeit 
import random

"""The goal in this exercise is to measure in real time the efficiency of various sorting algorithms and to compare them. 
You will write some code and time how quickly it runs. 
You will be asked to graph the measurements you take. 
You should write this code in a single file and submit it here. 
On paper, you should turn in the graphs, explanations, and any other data that you produce as requested below.
"""

def randomreturn(n):
    #placeholderlst = range(0, n)
    placeholderlst = [0]* (n)
    anotherplaceholder = list(range(1, n+1))
    i = 0
    while i < len(placeholderlst):
        item = random.choice(anotherplaceholder)
        #q = random.randint(0, len(fakealphabet)-1)
        placeholderlst[i] = item
        anotherplaceholder.remove(item)
        i +=1
    return placeholderlst    

    

def bubblesort(xs):
    n = len(xs)
    for passval in range(1, n):
        i = 0 #windows left position
        while i < n-passval:
            if xs[i] > xs[i-1]:
                xs[i], xs[i-1] = xs[i-1], xs[i] #swapthem
            i +=1


def selectionsort(xs): 
    for i in range(len(xs)):
        mini = min(xs[i:]) #find minimum element
        min_index = xs[i:].index(mini) #find index of minimum element
        xs[i + min_index] = xs[i] #replace element at min_index with first element
        xs[i] = mini                  #replace first element with min element
    #print xs

def merge(ls,rs,xs):
    xi, li, ri = 0, 0, 0 
    while xi < len(xs): 
        l_valid, r_valid = li < len(ls), ri < len(rs) 
        if l_valid and ((not r_valid) or ls[li] <= rs[ri]): 
            xs[xi] = ls[li] 
            li += 1 
        else: 
            xs[xi] = rs[ri] 
            ri += 1 
        xi += 1 


def mergesort(xs):
    if len(xs) > 1:
        middle = len(xs) // 2 
        lefts = xs[:middle] 
        rights = xs[middle:] 
        mergesort(lefts) 
        mergesort(rights) 
        merge(lefts,rights,xs) 


def quicksort_helper(xs, left, right): 
    if left < right: 
        pivot = partition(xs, left, right) 
        quicksort_helper(xs, left, pivot - 1) 
        quicksort_helper(xs, pivot + 1, right) 

def partition(xs, first, last): 
    pivot, pivot_value = first, xs[first] #*
    #Pick a rand index from l to r. Use that value at that index as pivot? *
    #Pick median of left, middle(l+r)//2, and right value, pick median of those three as pivot value? *
    #Use knowlege of distribution to inform split? [But not really. No one does this.]
    #Scan data, compute median from those values? (Takes at least linear time, its too much time, no one does this.)
    i = first + 1 
    while i <= last: 
        if xs[i] <= pivot_value: 
            xs[pivot+1],xs[i] = xs[i],xs[pivot+1] 
            pivot = pivot + 1 
        i += 1 
    xs[first],xs[pivot] = xs[pivot],xs[first] 
    return pivot 


def quicksort(xs): #MAKE A QUICKSORT THAT DOESN'T JUST CHOOSE LEFTMOST VALUE? Be careful choosing pivot val
    quicksort_helper(xs, 0, len(xs)-1)


"""Now, you should write code that times how long it takes each algorithm to sort lists of various sizes. 
You should create a graph that shows a line representing each sort’s time as a function of the input length. 
Write a short note explaining how they compare at various input sizes and whether the lines you 
are getting are consistent with our theoretical expectations. 
You will find the timeit module useful for this.
"""


"""I recommend timing the algorithm sorting a number of lists of the same length 
and then averaging to find the typical time it takes the algorithm to sort a list of a certain length. 
That will give a more accurate estimate of the time it takes on average. 

Make sure you don’t include generating the randomly-ordered lists when you do the timing---you want to time only how long it takes to sort them. 
Repeat this timing and averaging procedure for a number of different list sizes. 
Choose enough different input sizes to get a good idea of the shape of the graph.
"""

#[1, 44, 0, 7, 12] [ 111, 13, 55, 90, 2] [10000, 400, 5827, 27, 404] [607, 3, 2, 70, 500] [9, 8, 7, 5, 3]

#def runthrough(alg1, listsize):
def runthrough(listsize):
    placeholderlst = [0]*listsize
    i = 0
    #numb1 = 0
    #numb2 = 0
    while i < listsize:
        placeholderlst[i] = randomreturn(listsize)
        i +=1


    #for i in placeholderlst:
        #numb1 += timeit.timeit(stmt=alg1(i),number=1000)
        #numb2 += timeit.timeit(stmt=alg2(i),number=1000)

    #    numb1 += timeit.timeit(stmt= "bubblesort(i)", number=1000)
        #numb1 += timeit.timeit(stmt=selectionsort(i), number=1000)
        #numb1 += timeit.timeit(stmt=mergesort(i), number=1000)
        #numb1 += timeit.timeit(stmt=quicksort(i), number=1000)

    #numb1 = numb1/listsize
    #numb2 = numb2/listsize
    #return numb1
    return placeholderlst

def timeafunctionbubble(number):
    #currently for bubblesort
    #placeholderlist = runthrough(number)
    settingup = ("from timing import bubblesort \n" + "from timing import runthrough \n" + "import random \n\n")
    settingup += "listofthings = []"
    settingup += "\nfor i in range(10):" + "\n"
    settingup += "\t"+ "listofthings.append(runthrough("+ str(number) + "))"
    '''
from timing import bubblesort
from timing import runthrough
import random

listofthings = []
for i in range(10):
    listofthings.append(runthrough(20))
'''
#Creating 10 lists of size 10

    mycode = '''
for i in listofthings:
    bubblesort(i)'''

    time = timeit.timeit(setup = settingup,
     stmt = mycode,
     number = 1000) 
    time = time/number #Averaging


    print("bubblesort time:" + str(time))


def timeafunctionselection(number):
    #currently for selectionsort
    settingup = ("from timing import selectionsort \n" + "from timing import runthrough \n" + "import random \n\n")
    settingup += "listofthings = []"
    settingup += "\nfor i in range(10):" + "\n"
    settingup += "\t"+ "listofthings.append(runthrough("+ str(number) + "))"

    '''
from timing import selectionsort
from timing import runthrough
import random

listofthings = []
for i in range(10):
    listofthings.append(runthrough(20))
'''
    mycode = '''
for i in listofthings:
    selectionsort(i)'''

    time = timeit.timeit(setup = settingup,

     stmt = mycode,

     number = 1000)
    time = time/number

    print("selectionsort time:" + str(time))

def timeafunctionmerge(number):
    #currently for mergesort
    #placeholderlist = runthrough(number)
    settingup = ("from timing import mergesort \n" + "from timing import runthrough \n" + "import random \n\n")
    settingup += "listofthings = []"
    settingup += "\nfor i in range(10):" + "\n"
    settingup += "\t"+ "listofthings.append(runthrough("+ str(number) + "))"

    '''
from timing import mergesort
from timing import runthrough
import random

listofthings = []
for i in range(10):
    listofthings.append(runthrough(100))
'''
    mycode = '''
for i in listofthings:
    mergesort(i)'''

    time = timeit.timeit(setup = settingup,

     stmt = mycode,

     number = 1000)
    time = time/number

    print("mergesort time:" + str(time))

def timeafunctionquick(number):
    #currently for quicksort
    settingup = ("from timing import mergesort \n" + "from timing import runthrough \n" + "import random \n\n")
    settingup += "listofthings = []"
    settingup += "\nfor i in range(10):" + "\n"
    settingup += "\t"+ "listofthings.append(runthrough("+ str(number) + "))"
    '''
from timing import quicksort
from timing import runthrough
import random

listofthings = []
for i in range(10):
    listofthings.append(runthrough(100))
'''
    mycode = '''
for i in listofthings:
    quicksort(i)'''

    time = timeit.timeit(setup = settingup,

     stmt = mycode,

     number = 1000)
    time = time/number

    print("quicksort time:" + str(time))


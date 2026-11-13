def partition(xs, first, last):
    pivot, pivot_value = first, xs[first]
    i = first + 1
    while i <= last:
        if xs[i] <= pivot_value:
            xs[pivot+1],xs[i] = xs[i],xs[pivot+1]
            pivot = pivot + 1
        i += 1
    xs[first], xs[pivot] = xs[pivot], xs[first]
    return pivot

def statistic_helper(i, aList, left, right):
    
        

    if left < right:
        pivot = partition(aList, left, right)
        #statistic_helper(i, aList, left, pivot - 1)
        #statistic_helper(i, aList, pivot + 1, right)
        left_count = len(aList[0:pivot])
        right_count = len(aList[pivot+1:])
        if left_count == i:
            return aList[pivot]
        elif left_count > i:
            return statistic_helper(i, aList, left, pivot - 1)
            #i-th order statistic element is sitting in left partition
        elif left_count < i:
            return statistic_helper(i, aList, pivot + 1, right)
            #ith order stat element in right partition. 
    elif left == i:
        #print(aList[left])
        return aList[left]

def statistic(i,aList):
    return statistic_helper(i, aList, 0, len(aList)-1)
    #returns the value that is the i-th order statistic of aList. 
    #You can assume that the list of values has no value appear more than once. 
    #You can also assume that i is non-negative and less than the length of aList.


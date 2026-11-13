#partner: hanheller
#partner: garciase

def fib3(n):
    prev, prev2, curr = 0, 0, 1
    i = 1
    while i <n:
        prev, prev2, curr = curr, prev+curr, prev2 + curr
        i +=1
    return curr
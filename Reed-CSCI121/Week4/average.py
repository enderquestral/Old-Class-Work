#hanheller
#no partner, due to being sick on the lab day



"""takes three parameters. The first is an integer function and the next two are integers. 
It should return the average value of function f when evaluated on numbers in the range from start up to end. 
That is, it should compute the sum f(start) + f(start+1) + ... + f(end) divided by the number of summands in that sum.

>>> average(lambda b: b*b, 1, 4)
7.5
>>> average(lambda b: b*b, 2, 4)
9.666666666666666
>>> average(lambda b: b*b, -1, 1)
0.666666666666666
>>> average(lambda a: a+10, 1,5)
13.0"""

def average(f,start,end):
    x = start
    total= 0
    while x <= end:
        total += f(x)
        x+= 1

    return (total /((end-start)+1))

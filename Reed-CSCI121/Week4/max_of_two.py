#hanheller
#no partner, due to being sick on the lab day


#three parameters. The first two are functions and the third is a number. 
#The function max_of_two should call each of the two functions f and g on the number x that was given. 
#It should return the maximum of those two results.

""">>> max_of_two(lambda a: a+10, lambda b: b*b, 2)
12
>>> max_of_two(lambda a: a+10, lambda b: b*b, 3)
13
>>> max_of_two(lambda a: a+10, lambda b: b*b, 4)
16
>>> max_of_two(lambda a: a+10, lambda b: b*b, 5)
25""" 

def max_of_two(f,g,x):
    item1= f(x)
    item2= g(x)
    if item1>item2:
        return item1
    elif item1 == item2:
        return item1
    else:
        return item2

def reverse_of(xs):
    if len(xs) ==0:
        return [] #return empty set
    else:
        return [xs[-1]] + reverse_of(xs[:-1]) #return spot at end of list, then cut off that point 
        
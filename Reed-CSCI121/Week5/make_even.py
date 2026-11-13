#partner: hanheller
#partner: omkazmi

def make_even(xs):

    n = 0
    while n < len(xs):
        
        if xs[n] % 2 ==0:
            pass
        else:
            xs[n] = xs[n]-1
        n +=1

    return None
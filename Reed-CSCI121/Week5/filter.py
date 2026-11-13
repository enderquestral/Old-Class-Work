#partner: hanheller
#partner: omkazmi

def filter(test, xs):
    newlist = []
    n = 0
    while n < len(xs):
        torf = test(xs[n])
        if torf == True:
            newlist.append(xs[n])
        n += 1
    return newlist

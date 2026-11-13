#partner: hanheller
#partner: omkazmi

#n is a pos int, xs is a list of ints that are all pos, and range from 0 to n-1
def counts(n, xs):
    newlist = []

    c = 0
    while c < n:
        newinstance = 0
        for x in xs:
            if x == c:
                newinstance +=1

        newlist.append(newinstance)

        c +=1

    return newlist
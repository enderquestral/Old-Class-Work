#partner: hanheller
#partner: thomsonc

#NO USE OF WHILE LOOP IN CODE
#DOES NOT WORK HERE)
def remainder(n,d):
    if (n<d) and n>=0:
        return n

    if n >0:
        n = n-d
    elif n<0:
        n = n+d
    return remainder(n,d)
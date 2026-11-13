
def createRational(n,d):
    return [n,d]

def numerator(r):
    return r[0]

def denominator(r):
    return r[1]

def sameRationals(r,s):
    nr = numerator(r)
    dr = denominator(r)
    ns = numerator(s)
    ds = denominator(s)
    return (nr * ds == ns * dr)

def outputRational(r):
    n = numerator(r)
    d = denominator(r)
    ntext = str(n)
    dtext = str(d)
    print(ntext + "/" + dtext)

def sumRationals(r,s):
    nr = numerator(r)
    dr = denominator(r)
    ns = numerator(s)
    ds = denominator(s)
    return createRational(nr*ds + ns*dr, dr*ds)

def productRationals(r,s):
    nr = numerator(r)
    dr = denominator(r)
    ns = numerator(s)
    ds = denominator(s)
    return createRational(nr*ns, dr*ds)

R = createRational
e = sameRationals
s = sumRationals
p = productRationals
o = outputRational
n = numerator
d = denominator



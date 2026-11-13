
def GCD(a,b):
    if a < b:
        a,b = b,a
    if b < 0:
        b *= -1
    while b > 0:
        a,b = b,a%b
    return a

def createRational(n,d):
    if d < 0:
        n *= -1
        d *= -1

    g = GCD(n,d)

    num = n // g
    den = d // g

    def theRational(which):
        if which == 'top':
            return num
        elif which == 'bottom':
            return den
        else:
            return None

    return theRational

def numerator(r):
    return r('top')

def denominator(r):
    return r('bottom')

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
    width = max(len(ntext)+2,len(dtext)+2)
    npad = width-len(ntext)
    dpad = width-len(dtext)
    print((npad // 2)*" " + ntext)
    print("-"*width)
    print((dpad // 2)*" " + dtext)
    print()

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




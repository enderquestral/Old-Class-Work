
def GCD(a,b):
    if a < b:
        a,b = b,a
    if b < 0:
        b *= -1
    while b > 0:
        a,b = b,a%b
    return a

class Rational:

    def __init__(self,n,d):
        if d < 0:
            n *= -1
            d *= -1
        g = GCD(n,d)
        self.num = n // g
        self.den = d // g

    def numerator(self):
        return self.num

    def denominator(self):
        return self.den

    def __eq__(self,other):
        ns = self.numerator()
        ds = self.denominator()
        no = other.numerator()
        do = other.denominator()
        return (ns * do == no * ds)

    def __str__(self):
        n = self.numerator()
        d = self.denominator()
        ntext = str(n)
        dtext = str(d)
        if d == 1:
            return ntext
        else:
            return ntext + "/" + dtext

    def __add__(self,other):
        ns = self.numerator()
        ds = self.denominator()
        no = other.numerator()
        do = other.denominator()
        return Rational(ns*do + no*ds, ds*do)

    def __mul__(self,other):
        ns = self.numerator()
        ds = self.denominator()
        no = other.numerator()
        do = other.denominator()
        return Rational(ns*no, ds*do)





from Rational import Rational

r0 = Rational(0,1)
r1 = Rational(3,4)
r2 = Rational(2,3)
r3 = r1.sumWith(r2)
r4 = r1.productWith(r2)
r5 = r3.sumWith(r4)
r6 = Rational(3,3)
print(r1.stringOf())
print(r2.stringOf())
print(r3.stringOf())
print(r4.stringOf())
print(r5.stringOf())
print(r6.stringOf())
print(r1.equals(r2))
print(r1.equals(r0.sumWith(r1)))
print(r1.equals(r1.productWith(r6)))

print()
# In case you are curious:
print()

R = Rational
e = Rational.equals
s = Rational.sumWith
p = Rational.productWith
o = lambda r: print(r.stringOf())
n = Rational.numerator
d = Rational.denominator

r0 = R(0,1)
r1 = R(3,4)
r2 = R(2,3)
r3 = s(r1,r2)
r4 = p(r1,r2)
r5 = s(r3,r4)
r6 = R(3,3)
o(r1)
o(r2)
o(r3)
o(r4)
o(r5)
o(r6)
print(e(r1,r2))
print(e(r1,s(r0,r1)))
print(e(r1,p(r1,r6)))



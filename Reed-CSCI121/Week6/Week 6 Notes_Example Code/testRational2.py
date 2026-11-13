
from Rational2 import Rational

r0 = Rational(0,1)
r1 = Rational(3,4)
r2 = Rational(2,3)
r3 = r1 + r2
r4 = r1 * r2
r5 = r3 + r4
r6 = Rational(3,3)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r1 == r2)
print(r1 == r0+r1)
print(r1 == r1*r6)

print()
# In case you are curious:
print()

R = Rational
e = Rational.__eq__
s = Rational.__add__
p = Rational.__mul__
o = lambda r: print(r)
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



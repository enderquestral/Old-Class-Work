
from rational_as_list import *

R = createRational
e = sameRationals
s = sumRationals
p = productRationals
o = outputRational
n = numerator
d = denominator

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


#partner: hanheller
#partner: omkazmi

def reverse(x): #Given int x, assume x is 3 digits, assume x is not divisible by 10, assume x >100 & <1000
    a = x // 100 #normal 100s place
    b = (x // 10) % 10
    c = x % 10 #normal 1s place
    return (c*100)+(b*10)+a
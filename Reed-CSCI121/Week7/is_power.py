#partner: hanheller
#partner: thomsonc

def is_power(n,b):
    #2^x = 16
    if n==1:
        return True
    elif n==b:
        return True

    if b<= 0:
        return False

    if n%b ==0:
        return is_power(n//b, b)

    return False

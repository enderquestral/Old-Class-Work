#computes the quotient n//d
#using same ideas used in remainder

def quotient(n,d):
    if n==0 or d==0:
        return 0

    if n == d or n <d:
        if n ==d:
            return 1
        elif abs(n) <d:
            if n>=1:
                return 0
            else:
                return -1

    if n >0:
        n = n-d
        return quotient(n,d) +1
    elif n<0: 
        n = n+d
        return quotient(n,d) -1


#partner: hanheller
#partner: thomsonc

def collatz_length(n):
    if n==1:
        return 1
    else:
        if n%2 ==0:
            n = n//2
        else:
            n = (n*3) +1
#        print(n)

        return collatz_length(n) + 1

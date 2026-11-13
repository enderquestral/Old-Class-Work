#non-neg int, returns a list of the first n primes

def primes_list(n):
    newlist = []
    num = 0
    while n > 0:
        num +=1
       # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                newlist.append(num)
                n -=1

    return newlist
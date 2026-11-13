def collatz(n):
    #Start with pos int
    #if number is odd, multiply by 3 and add 1. If its even, divide by 2. 
    #keep this loop up until we result in 1.
    #returns the first int for which the generated sequence is at least n in length.
    # EX: input 6. sequence: 6, 3, 10, 5, 16, 8, 4, 2, 1. sequence length 9. outputs 3.
    # Trying to find an int with collat squence equal to the value of n
    # 10, 5, 16, 8, 4, 2, 1. Sequence length 7. outputs 7. ??????

    # 7, 22, 11, 34, 17, 52. 26. 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. Length 17.
    #collatz(10) outputs 7 because it is the first number whose sequence length is great/equal to 10
    # can write a helper function for this 
    
    #Handle 0 somehow, to get 1?

    inputvalue = n
    firstint = 0
    firstrun = True
    i =1
    while firstrun:
        inputvalue = findseqlen(i)
        if inputvalue >= n:
            firstint = i
            firstrun= False
        i+=1
    return firstint


def findseqlen(n):
    sequencelen2 = 1
    while n!=1:
        if n%2 ==0:
            n=n//2
        else:
            n = (n*3)+1
        sequencelen2 +=1

    return sequencelen2
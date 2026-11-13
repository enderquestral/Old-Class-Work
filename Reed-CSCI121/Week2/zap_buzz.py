    #Each person takes a turn saying a number, counting upwards from 1.
    #If a multiple is a number of seven, they say zap instead of a number
    #If the number has a digit of 3, they say buzz
    #If both are true, say zap buzz
    #GIVEN A POSITIVE INTEGER PARAMETER, LESS THAN 1000
def zap_buzz(x):
    boolcool = False
    count = 0
    n = x
    while (n> 0):
        n = n//10
        count = count + 1
    
    for y in range(count): #may need to start the range with a 1?
        if ((x // (10**y)) %10) == 3:
            boolcool = True
    if boolcool & (x%7 == 0):
        return "zap buzz"
    elif boolcool:
        return "buzz"
    elif (x%7 == 0):
        return "zap"
    else:
        return x
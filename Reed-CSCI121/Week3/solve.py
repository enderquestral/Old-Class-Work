def solve(a,b,c):
    # choose a,b,c, a is nonzero, and x varries. 
    #quadratic equation a*x**2 + b*x + c ==0, solutions below
    #x = (-b +sqrt(b**2 -4*a*c)) / 2*a
    #x = (-b -sqrt(b**2 -4*a*c)) / 2*a
    #The two arbove are the same if b**2 -4*a*c == 0. No solutions if that is negative.
    #Discriminant must be square, division must yield a whole number
    
    #Function is to give largest int x  with those three int coefficients
    #If no int solution to that equation, return false
    # use // for division. Make sure division yields int (using %)
    #use own code to compute square root as an int, dont use math.sqrt or **0.5
    
    numb1 = 0 #+sqrt
    numb2 = 0 #-sqrt
#Should return 0 for 1,1,0 not False
    canbesquared = helpsqrt(a,b,c)
    if canbesquared > 0: #When canbe == 20, and b is 0 and a is 100...
        numb1 = (-b + canbesquared)%(2*a) #Check if it is an int? Throw it out if it's not. 
        numb2 = (-b - canbesquared)%(2*a) #Use % and if it's not 0, then throw out

        if numb1 >0 and numb2 >0: #to check if they're a float less than 1
            return False
        elif numb1>0 and numb2<=0: #numb1 has a remainder and numb2 does not
            numb2 = (-b - canbesquared)//(2*a) 
            numb1 = numb2 -1
        elif numb1<=0 and numb2>0:
            numb1 = (-b + canbesquared)//(2*a)
            numb2 = numb1 -1
        else:   
            numb1 = (-b + canbesquared)//(2*a)
            numb2 = (-b - canbesquared)//(2*a) 

        if numb1 >numb2:
            return numb1
        else: 
            return numb2
    elif canbesquared == 0:# numb1 == numb2
        return -b //(2*a)
    else:
        return False

def helpsqrt(a,b,c):
    tobesquared = (b**2 - 4*a*c)
    if tobesquared ==0:
        return 0
    elif tobesquared < 0:
        return -1

    placeholder1 = -1
    i = 0
    while i < tobesquared:
        if i**2 == tobesquared:
            placeholder1 = i
        elif ((i+1)**2) == tobesquared:
            placeholder1 = i+1
        i+=2
    
    return placeholder1

#sqrt 132.
# 137 != 12*13
# 11**2 (121) AND 12**2 (144)
# SEE IF A SQUARE WORKS
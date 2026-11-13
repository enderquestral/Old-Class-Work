def numpal(n):
    #Takes non-neg int, returns True if digit sequence is a pelindrome. False otherwise.
    #Dont use strings, use // and % to perform this
    if n //10 ==0: #if it is a single digit
        return True
    else:
        timesten =1 #has at least 2 digits
        leftspot =0
        rightspot = 0
        while (n//timesten) >= 10:
            timesten = timesten * 10 #Finding out how many digits there are (save for 1)

        while n !=0:
            leftspot = n//timesten #Checking a chunk off the left, with the help from timesten
            rightspot = n%10 #checking chunk from right
            if leftspot != rightspot and n >9:
                return False
            n = (n%timesten) //10
            timesten = timesten // 100
        return True
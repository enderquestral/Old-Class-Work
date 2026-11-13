def poly2max(x1, x2, y1, y2):
    # USING : z = -x**4 + 3*x**2 = y**4 + 5*y**2
    firstRound = True
    currentmax = 0
    placeholder = 0
    for i in range(x1, x2 +1):
        for v in range(y1, y2 +1):
            placeholder = -i**4 + 3*i**2 - v**4 + 5*v**2
            if firstRound:
                currentmax = placeholder
                firstRound =False
            if placeholder > currentmax:
                currentmax = placeholder
    #Minimum and maximum values for x and y. 
    #Should return the maximum value z takes for any x and y chosen from those ranges
    # EX: poly2max(0,5,3,7)  would search thru values of x from 0 to 5 (including both 0 and 5) using values of y from 3 to 7 to find this polynomial function's largest value
    # poly2max(0,5,0,10) >>> 6
    return currentmax
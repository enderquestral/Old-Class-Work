def maxSublist(listofint):
    #returns sublist of max total sum
    #sublist is contiguous portion of list. Sublist at least 1.
    i = 0
    currentlst = [listofint[0]]
    maxtotal = listofint[0]
    while i < len(listofint)-1:
        
        j = i
        while j < len(listofint):
            #if maxtotal < maxtotal + listofint[j]:
            sumcursublist = sum(listofint[i:j+1])
            if maxtotal < sumcursublist:
                maxtotal = sumcursublist
                currentlst = listofint[i:j+1]
            #Somehow make a random choice?
            j +=1
        i +=1

    if len(currentlst) == 2:
        if currentlst[0] < 0 and currentlst[0] < currentlst[1]:#is negative
            currentlst = [currentlst[1]]
        elif currentlst[1] <0 and currentlst[1] < currentlst[0]:
            currentlst = [currentlst[0]]

    return currentlst
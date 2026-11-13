def twoSum(listofint, targetval):
    #return true if two nums in list add up to target val
    #false if not
    #if list is len1 or less, return false

    if len(listofint) >1:
        i = 0
        while i < len(listofint)-1:
        #for i in listofint:
            j = i+1
            while j < len(listofint):
            #for j in listofint[]:
                currentval = listofint[i] +listofint[j]
                if currentval == targetval:
                    return True
                j +=1
            i +=1
        return False
    else:
        return False


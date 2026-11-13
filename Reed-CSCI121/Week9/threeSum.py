def threeSum(listofint, targetval):
    #return true if 3 nums in list add up to target val

    if len(listofint) >2:
        i = 0
        #lenlist = len(listofint)
        while i < len(listofint) -2:
        #for i in listofint:
            k = i+1
            while k < len(listofint) -1:
                j = k+1
                while j < len(listofint):
                #for j in listofint[]:
                    currentval = listofint[i] +listofint[k] + listofint[j]
                    if currentval == targetval:
                        return True
                    j +=1
                k +=1
            i +=1
        return False
    else:
        return False


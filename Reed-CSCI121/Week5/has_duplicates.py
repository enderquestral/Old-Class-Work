#takes a list xs and determines whether some value appears more than once. 
#It should return True if so, and False if there are no reoccurring values. Note that the list xs could be empty.

#consider strings? bools?
def has_duplicates(xs):

    newlist =[]
    if len(xs) >1:
        x = 0
        while x < len(xs):
            y = 0
            while y < len(newlist):
                if xs[x-1] == newlist[y]:
                    return True
                y +=1
            newlist.append(xs[x-1])
            x +=1

    return False


    #Check if xs[n] is in all of newlist as it exists, and if it is then return True
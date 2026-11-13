def char_count(s):
    #eturns a dictionary with keys corresponding to the characters 
    #which appear in the string and values corresponding the frequency with which they appear. 
    newdict = {}
    i = 0
    while i < len(s):
        if s[i] in newdict:
            newdict[s[i]] = newdict[s[i]] +1
        else:
            newdict.update({s[i] : 1})
        i +=1

    return newdict
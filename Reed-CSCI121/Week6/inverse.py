def inverse(d):
    newdict = {}
    for key in d:
        if d[key] in newdict:
            newdict[d[key]].append(key)
        else:
            newdict.update({d[key] : [key]})
            

    return newdict

#Input dictionary returns its "inverse" dictionary, a dictionary mapping values of entries in the given dictionary 
#to lists of keys in the given dictionary. 
#That is, it returns a dictionary whose keys are the values of the original dictionary and whose entries are lists 
#of keys which mapped to that value in the original dictionary.

#assume the dictionary you are given has strings both as keys and as values.
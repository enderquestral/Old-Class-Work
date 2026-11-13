def countsort(aList, m):
    #list values are from 0 to m-1

    #Answer the following question: What is the running time of your countsort code? Include a comment in your code describing the running time of your function.
    #It runs in O(n+k) time. O(n+k) because n is the number of elements in the input list, with k being the range of the input (0 to m-1). 
    #Would have thought it would run O(n^2) because of the for loop within a for loop, but I suppose not no because one of those for loops is range m.

    count = [0]* (m)  # Init it to proper size

    for a in aList:
        count[a] +=1 #instance of a variable happening
    #print(count)
    i = 0
    for b in range(m):
        for c in range(count[b]):
            aList[i] = b
            i +=1
    print(aList)

    #Given a list of numbers (not ordered) and how many times they appear. 

    #for each value in setuplist, go through aList in it's entirety, and if you find an instance of a value, put it at the "end" of the covered area. 





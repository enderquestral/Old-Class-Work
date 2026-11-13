def insertion_sort(xs):
    #Code should not return anything, instead modifying what is given
    #Answer the following question: What is the running time of this sorting algorithm? Turn in this (brief) analysis along with your report for the timing exercise (Problem 4) described below.
    #After first pass, slot 0 and slot 1 will be in sorted order 
    #In the second insertion pass, it places xs[2] in the appropriate place within the first three slots (slot 0, slot 1, slot 2) so that they are in sorted order.
    #With the third insertion pass, it places xs[3] in the appropriate place within the first four slots (slot 0, slot 1, slot 2, slot 3) so that they are in sorted order.


    print(xs)

    for i in range(1,len(xs)):
        place = i 
        point = xs[i]


        while place > 0 and xs[place - 1] > point:
            xs[place] = xs[place - 1]
            place = place - 1

        xs[place] = point

        print(xs)
        

#Answer the following question: What is the running time of this sorting algorithm? Turn in this (brief) analysis along with your report for the timing exercise (Problem 4) described below.



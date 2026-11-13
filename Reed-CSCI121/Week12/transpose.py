#partner: hanheller
#partner: 
def transpose(infile, outfile):
    # file contents consist of a header line that is a pair of integers separated by a space. 
    #The subsequent lines give a table of digit values, with a number of rows equal to the first integer, 
    #and a number of columns given by the second integer.


    #You can assume that there is at least one row and at least one column. 
    #Having read in the file, the transpose function should then write out a file 
    #named by the string given by outfile with the table "flipped" along its diagonal. 
    
    newfile = open(outfile, "w")

    with open(infile, "r") as f:

        listnotkey = [x.split(" ") for x in f]
        newfile.write(str(listnotkey[0][1]).strip() + " " + str(listnotkey[0][0]) + "\n")
        del listnotkey[0]
        for x in zip(*listnotkey):
            i = 0
            for y in x:
                newfile.write(y.strip())
                if i != len(x)-1:
                    newfile.write(" ")
                i +=1
            newfile.write("\n")

    f.close()
    newfile.close()
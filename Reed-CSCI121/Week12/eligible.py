#partner: hanheller
#partner: 
def eligible(infile, outfile):
    #Assume infile already exists
    #write out a (new) file named by the string specified as outfile, the second string parameter given 
    #That output file's contents should be the same as the file that was input, except that people that are too young to be eligible to vote (under the age of 18) should not be included.
    #f = open(infile, "r")
    newfile = open(outfile, "w")
    with open(infile, "r") as f:
        for x in f:
            y = x.split(", ")
            if int(y[1]) >= 18:
                newfile.write(x)

    f.close()

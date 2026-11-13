#partner: hanheller
#partner: garciase
#pyramid(3) returned ' *\n * *\n * * *\n' but expected ' *\n * *\n* * *\n'
# Printed '   *\n  * *\n * * *\n'
#         '   *\n  * *\n * * *\n'
#                                   '  *\n * *\n* * *\n'



def pyramid(h):
    i =1
    emptystr = ""
#    if h ==1:
#        emptystr = "*"+"\n"
#        return emptystr
    while i <= h:
        emptystr = emptystr + ((" " * (h-i)) + ("* "*(i-1)) + ("*") + "\n")
        i+=1 
    #print(emptystr)
    return emptystr

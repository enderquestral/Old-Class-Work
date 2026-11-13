#partner omkazmi
#partner hanheller

def check_multiple(a, b):# use absolute value?
    if b == a: # -8, -2, is a multiple
        return("Is a multiple.")
    else: 
        if b > 0:
            if a % b == 0: 
             return("Is a multiple.")
            else : 
                return ('Not a multiple.')
        elif b <0 and a<0:
            if a % b ==0:
                return("Is a multiple.")
            else:
                return("Not a multiple.")
        else:
            return("Not a multiple.")
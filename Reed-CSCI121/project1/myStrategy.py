#hanheller

def myStrategy(myscore, theirscore, last): #AVERAGE ROLL IS 2.5, 3.5 if you want to be aggressive

    safereturn = (100-myscore)//3

    if myscore ==0: #First turn for me
        if theirscore >0: #go second
            return safereturn 
        else: #go first
            return 33

    elif last == True: #if it's the last turn
        if theirscore > myscore:
            if (theirscore - myscore) < 3:
                return 1 
            return safereturn
        elif theirscore == myscore:
            return safereturn
        else: #My score is greater than theirs
            return 0  

    else: #If they've NOT quit yet
        if theirscore > myscore: #If their score is larger than mine 
            if myscore >= 99: 
                return 0
            elif myscore >= 95:
                return 1
            elif myscore >= 90:
                return safereturn -1
            else: 
                return safereturn
            #return safereturn
        elif theirscore == myscore: #If their score is the exact same as mine
            if myscore >= 99: 
                return 0
            elif myscore >= 95:
                return 1
            elif myscore >= 90:
                return safereturn
            else:
                return safereturn +1
            #return safereturn
        elif theirscore < myscore: #If their score is less than mine
            if myscore >= 98: 
                return 0
            #elif myscore >= 97:
            #    return 1
            elif myscore >= 94:
                return safereturn 
            else:
                return safereturn
        else: 
            return 0 #0 because something went wrong
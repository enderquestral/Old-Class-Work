#log10(n)^2 == (log10(n))^2

def longPalSub(inputstr):
    if len(inputstr) >1:
        maxLen = 1
        start = 0
        low=0
        high = 0
        for i in range(1, len(inputstr)):
            low = i-1
            high = i
            while low >=0 and high <len(inputstr) and inputstr[low] == inputstr[high]:
                if high-low +1 > maxLen:
                    start = low
                    maxLen = high - low+1
                low -=1
                high +=1
            low = i-1
            high = i +1
            while low >=0 and high <len(inputstr) and inputstr[low] == inputstr[high]:
                if high-low +1 > maxLen:
                    start = low
                    maxLen = high - low+1
                low -=1
                high +=1

        return inputstr[start:start+maxLen]
    else:
        return inputstr


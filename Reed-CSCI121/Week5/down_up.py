#partner: hanheller
#partner: 

#n is a pos int
#account for 0 set?
def down_up(n):
    i = n
    counts = []
    while len(counts) !=n:
        counts.append(i)
        i +=1
    i =1
    while n<= len(counts) < n*2 -1:
        i = i+1
        counts.append(i)
    return counts
def digit(x,n): # 10^2 == 100
    count = 0
    var = n
    while (n> 0):
        n = n//10
        count = count + 1

    if n > count:
        return 0
    else:
        y = (x // (10**var)) %10
        return y

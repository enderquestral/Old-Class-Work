def coins(x):
    #Prints the number of US coins (quarters, dimes, nickles, pennies) needed
    cents = x
    quarternum = 0
    dimenum = 0
    nicklenum = 0
    pennynum = 0 #Maybe count out amount of each coin, subtract penny ammount by nickleam *5, dime*10...
    #GOTTA FIND OUT HOW TO GET THE NUMBER FROM A %
    total = 0

    if cents % 25 == 0: #QUARTERS
        while cents > 0:
            cents = cents - 25
            quarternum = quarternum +1
    else: 
        while cents > (cents%25):
            cents = cents - 25
            quarternum = quarternum +1
            
            
    if cents % 10 == 0: #DIME
        while cents > 0:
            cents = cents - 10
            dimenum = dimenum +1
    else: 
        while cents > (cents%10):
            cents = cents - 10
            dimenum = dimenum +1
            
    if cents % 5 == 0: #nickle
        while cents > 0:
            cents = cents - 5
            nicklenum = nicklenum +1
    else: 
        while cents > (cents%5):
            cents = cents - 5
            nicklenum = nicklenum +1
            
    #NEED ALT LOOP FOR PENNIES?
    pennynum = cents
    total = quarternum + dimenum + nicklenum +pennynum

    return total
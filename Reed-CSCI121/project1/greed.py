import random
import math
import pr1testing
random.seed()

# CSCI 121 Fall 2017
# 
# Project 1: Game of Greed starting code.
#
# See the project description on the web.
# 
# You can play an game of Greed with an opponent by running 
# something like the following in the terminal:
#
#     python3 -i greed.py
#     >>> play()
#
# This 'play' function will ask for your two names, and then
# offer Player 1 to take a turn, then Player 2, etc.
#
# Several function templates follow, ones that you are asked
# to complete for this assignment.
#
# You'll turn this in at the cs.reed.edu CSHW/VRFY submission
# site.
#

def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1? ")
    player2 = input("Name of Player 2? ")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print("It is " + player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll? "))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        print("Dice rolled:" + diceString)
        print("Total for this turn: " + str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print("It is " + player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll? "))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        print("Dice rolled:" + diceString)
        print("Total for this turn: " + str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2): ##EDIT THIS
    player1 = "Player 1"
    player2 = "Player 2"
    score1 = 0
    score2 = 0
    last = False #USE THIS FOR IF SOMEONE PASSED
    player1stat = strat1(score1, score2, last)
    player2stat = strat2(score2, score1, last)
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print("It is " + player1 + "'s turn.")
        numDice = player1stat
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        print("Dice rolled:" + diceString)
        print("Total for this turn: " + str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        player1stat = strat1(score1, score2, last)
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print("It is " + player2 + "'s turn.")
        numDice = player2stat
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " " + str(d)
            i = i-1
        print("Dice rolled:" + diceString)
        print("Total for this turn: " + str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
        player2stat = strat2(score2, score1, last)
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3


def autoplay(strat1, strat2): #Have it return the value 1 if the first player (the strategy listed in the first argument) wins. It should return 2 if instead the second player wins. Return a 3 when it's a tie.
    score1 = 0
    score2 = 0
    last = False 
    player1stat = strat1(score1, score2, last)
    player2stat = strat2(score2, score1, last)
    while True:
        numDice = player1stat
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        player1stat = strat1(score1, score2, last)
        numDice = player2stat
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
        player2stat = strat2(score2, score1, last)
    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3

def manyGames(strat1, strat2, n): #EDIT THIS
    p1wins = 0
    p2wins = 0
    tiesnum = 0
    oneisfirst = True
    for runs in range(0,n):
        if oneisfirst:
            placeholder = autoplay(strat1, strat2)
        else:
            placeholder = autoplay(strat2, strat1)

        if placeholder == 1:
            p1wins = p1wins +1
        elif placeholder ==2:
            p2wins = p2wins +1
        else:
            tiesnum = tiesnum +1
    print("Player 1 wins: " + "\t" + str(p1wins))
    print("Player 2 wins: " + "\t" + str(p2wins))
    print("Ties: " + "\t" + str(tiesnum))

def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
       return 12

def sample2(myscore, theirscore, last):
    if myscore <= 50:
        return 30
    elif myscore >= 51 and myscore <= 80:
        return 10
    else:
        return 0
#NOTE: Many tests were saved for later that are not present in this file, so the naming conventions are off
def test1(myscore, theirscore, last): #First attempt at myStrat, accounting for last, and where my score is. 
    if last: #if it's the last turn
        if theirscore > myscore:
            if myscore <= 50:
                return 12
            elif myscore > 80:
                return 6
            else: 
                return 9
        elif theirscore == myscore:
            if myscore >= 80:
                return 3
            elif myscore >= 60:
                return 6
            elif myscore >= 40:
                return 9
            elif myscore >= 20:
                return 10
            else:
                return 12
        else:
            return 0
    else: #If they've NOT quit yet
        if theirscore > myscore: #edit the 0s from here on 
            if myscore >= 80:
                return 1
            elif myscore >= 60:
                return 3
            elif myscore >= 40:
                return 4
            elif myscore >= 20:
                return 5
            else: #Less than 20
                return 6
        elif theirscore == myscore:
            if myscore >= 80:
                return 1
            elif myscore >= 60:
                return 2
            elif myscore >= 40:
                return 3
            elif myscore >= 20:
                return 4
            else:
                return 5
        elif theirscore < myscore:
            if myscore >= 80:
                return 0
            elif myscore >= 60:
                return 2
            elif myscore >= 40:
                return 3
            elif myscore >= 20:
                return 5
            else:
                return 9
        else: 
            return 0 #0 because something went wrong

def test4(myscore, theirscore, last): #First attempt at playing with theirscore-myscore
    if last: #if it's the last turn
        if theirscore > myscore:      
            if myscore >= 80: #Range 80 onwards
                if theirscore-myscore >= 20:
                    return 4
                elif theirscore-myscore >= 10:
                    return 2
                else:
                    return 1
            elif myscore >= 60: #range 60 to 79
                if theirscore-myscore >= 40:
                    return 9
                elif theirscore-myscore >= 30:
                    return 7
                elif theirscore-myscore >= 20:
                    return 5
                elif theirscore-myscore >= 10:
                    return 3
                else:
                    return 1
            elif myscore >= 40: #range 40 to 59
                if theirscore-myscore >= 60:
                    return 13
                elif theirscore-myscore >= 50:
                    return 11
                elif theirscore-myscore >= 40:
                    return 9
                elif theirscore-myscore >= 30:
                    return 7
                elif theirscore-myscore >= 20:
                    return 5
                elif theirscore-myscore >= 10:
                    return 3
                else:
                    return 1               
            elif myscore >= 20: #range 20  to 39
                if theirscore-myscore >= 80:
                    return 17
                elif theirscore-myscore >= 70:
                    return 15
                elif theirscore-myscore >= 60:
                    return 13
                elif theirscore-myscore >= 50:
                    return 11
                elif theirscore-myscore >= 40:
                    return 9
                elif theirscore-myscore >= 30:
                    return 7
                elif theirscore-myscore >= 20:
                    return 5
                elif theirscore-myscore >= 10:
                    return 3
                else:
                    return 1
            elif myscore >= 10: #range 10 to 19
                if theirscore-myscore >= 90:
                    return 19
                elif theirscore-myscore >= 80:
                    return 17
                elif theirscore-myscore >= 70:
                    return 15
                elif theirscore-myscore >= 60:
                    return 13
                elif theirscore-myscore >= 50:
                    return 11
                elif theirscore-myscore >= 40:
                    return 9 
                elif theirscore-myscore >= 30:
                    return 7
                elif theirscore-myscore >= 20:
                    return 5
                elif theirscore-myscore >= 10:
                    return 3
                else:
                    return 1

            else: #Somewhere from range 0 to 9
                return 20

        elif theirscore == myscore: 
            if myscore >= 80:
                return 4
            elif myscore >= 60:
                return 7
            elif myscore >= 40:
                return 8
            elif myscore >= 20:
                return 10
            else:
                return 15
        else: #My score is greater than theirs
            return 0
    else: #If they've NOT quit yet
        if theirscore > myscore: #If their score is larger than mine 
            if myscore >= 80:
                if theirscore-myscore >5:
                    return 2
                elif theirscore-myscore <5:
                    return 1
                else:
                    return 1
            elif myscore >= 60:
                if theirscore-myscore >5:
                    return 2
                elif theirscore-myscore <5:
                    return 2
                else:
                    return 1
            elif myscore >= 40:
                if theirscore-myscore >5:
                    return 2
                elif theirscore-myscore <5:
                    return 1
                else:
                    return 1
            elif myscore >= 20:
                if theirscore-myscore >5:
                    return 2
                elif theirscore-myscore <5:
                    return 2
                else:
                    return 1
            else: #Less than 20
                return 2
        elif theirscore == myscore: #If their score is the exact same as mine
            if myscore >= 80:
                return 0
            elif myscore >= 60:
                return 0
            elif myscore >= 40:
                return 1
            elif myscore >= 20:
                return 1
            else:
                return 1
        elif theirscore < myscore:#If their score is less than mine
            if myscore >= 80:
                return 0
            elif myscore >= 60:
                if myscore-theirscore >5:
                    return 0
                elif myscore-theirscore <5:
                    return 0
                else:
                    return 1
            elif myscore >= 40:
                if theirscore-myscore >5:
                    return 0
                elif theirscore-myscore <5:
                    return 1
                else:
                    return 1
            elif myscore >= 20:
                if theirscore-myscore >5:
                    return 0
                elif theirscore-myscore <5:
                    return 1
                else:
                    return 1
            else:
                return 2
        else: 
            return 0 #0 because something went wrontheirscore-myscoreat): #Confession: I know nothing about gambling

def testmess(myscore, theirscore, last): #Attemot at theirscore-myscore, and what that value is relating to how many dice are rolled
    if last == True: #if it's the last turn
        if theirscore > myscore: #Improve this section?      
            if theirscore-myscore >= 90:
                return 19
            elif theirscore-myscore >= 80:
                return 17
            elif theirscore-myscore >= 70:
                return 15
            elif theirscore-myscore >= 60:
                return 13
            elif theirscore-myscore >= 50:
                return 11
            elif theirscore-myscore >= 40:
                return 9 
            elif theirscore-myscore >= 30:
                return 7
            elif theirscore-myscore >= 20:
                return 5
            elif theirscore-myscore >= 10:
                return 3
            else:
                return 1
        elif theirscore == myscore: 
            if myscore >= 80:
                return 4
            elif myscore >= 60:
                return 7
            elif myscore >= 40:
                return 8
            elif myscore >= 20:
                return 10
            else:
                return 15
        else: #My score is greater than theirs
            return 0
    else: #If they've NOT quit yet
        if theirscore > myscore: #If their score is larger than mine 
            if myscore >= 80:
                if theirscore-myscore >= 20:
                    return 3
                elif theirscore-myscore >= 10:
                    return 2
                else:
                    return 0
            elif myscore >= 60:
                if theirscore-myscore >= 40:
                    return 6
                elif theirscore-myscore >= 30:
                    return 5
                elif theirscore-myscore >= 20:
                    return 4
                elif theirscore-myscore >= 10:
                    return 3
                else:
                    return 4
            elif myscore >= 40:
                if theirscore-myscore >= 60:
                    return 2
                elif theirscore-myscore >= 50:
                    return 3
                elif theirscore-myscore >= 40:
                    return 3
                elif theirscore-myscore >= 30:
                    return 4
                elif theirscore-myscore >= 20:
                    return 4
                elif theirscore-myscore >= 10:
                    return 5
                else:
                    return 5
            elif myscore >= 20:
                if theirscore-myscore >= 80:
                    return 9
                elif theirscore-myscore >= 70:
                    return 8
                elif theirscore-myscore >= 60:
                    return 8
                elif theirscore-myscore >= 50:
                    return 6
                elif theirscore-myscore >= 40:
                    return 6
                elif theirscore-myscore >= 30:
                    return 4
                elif theirscore-myscore >= 20:
                    return 4
                elif theirscore-myscore >= 10:
                    return 5
                else:
                    return 4 
            else: #Less than 20
                if theirscore-myscore >= 90:
                    return 20
                elif theirscore-myscore >= 80:
                    return 17
                elif theirscore-myscore >= 70:
                    return 15
                elif theirscore-myscore >= 60:
                    return 12
                elif theirscore-myscore >= 50:
                    return 9
                elif theirscore-myscore >= 40:
                    return 7
                elif theirscore-myscore >= 30:
                    return 6
                elif theirscore-myscore >= 20:
                    return 6
                elif theirscore-myscore >= 10:
                    return 5
                else:
                    return 5
        elif theirscore == myscore: #If their score is the exact same as mine
            if myscore >= 80:
                return 1
            elif myscore >= 60:
                return 2
            elif myscore >= 40:
                return 4
            elif myscore >= 20:
                return 6
            else:
                return 8
        elif theirscore < myscore:#If their score is less than mine
            if myscore >= 80:
                if myscore-theirscore >= 20:
                    return 2
                elif myscore-theirscore >= 10:
                    return 1
                else:
                    return 0
            elif myscore >= 60:
                if myscore-theirscore >= 40:
                    return 5
                elif myscore-theirscore >= 30:
                    return 7
                elif myscore-theirscore >= 20:
                    return 7
                elif myscore-theirscore >= 10:
                    return 5
                else:
                    return 8
            elif myscore >= 40:
                if myscore-theirscore >= 40:
                    return 2
                elif myscore-theirscore >= 30:
                    return 3
                elif myscore-theirscore >= 20:
                    return 4
                elif myscore-theirscore >= 10:
                    return 6
                else:
                    return 7
            elif myscore >= 20:
                if myscore-theirscore >= 30:
                    return 5
                elif myscore-theirscore >= 20:
                    return 6
                elif myscore-theirscore >= 10:
                    return 10
                else:
                    return 15
            else: #Less than 20
                if myscore-theirscore >= 20:
                    return 15
                elif myscore-theirscore >= 10:
                    return 10
                else:
                    return 10
        else: 
            return 0 #0 because something went wrong

def yetanothertest(myscore,theirscore,last): #Attempt to get the meand of myscore-theirscore
    #Get the mean of myscore - theirscore, roll whatever dice you need to try and get that
    if myscore >theirscore:
        goaldiceroll = (-1 * int((myscore-theirscore)//3.5))-1
    elif myscore<theirscore:
        goaldiceroll = int((theirscore-myscore)//3.5) +1
    else:
        goaldiceroll =1
    

    if last == True: #if it's the last turn
        if theirscore > myscore: #Improve this section?      
            if theirscore-myscore >= 90:
                return goaldiceroll + 9
            elif theirscore-myscore >= 80:
                return goaldiceroll + 8
            elif theirscore-myscore >= 70:
                return goaldiceroll + 7
            elif theirscore-myscore >= 60:
                return goaldiceroll + 6
            elif theirscore-myscore >= 50:
                return goaldiceroll + 5
            elif theirscore-myscore >= 40:
                return goaldiceroll + 4
            elif theirscore-myscore >= 30:
                return goaldiceroll + 3
            elif theirscore-myscore >= 20:
                return goaldiceroll + 2
            elif theirscore-myscore >= 10:
                return goaldiceroll + 1
            else:
                return 1
        elif theirscore == myscore: 
            if theirscore-myscore >= 90:
                return goaldiceroll + 9
            elif theirscore-myscore >= 80:
                return goaldiceroll + 8
            elif theirscore-myscore >= 70:
                return goaldiceroll + 7
            elif theirscore-myscore >= 60:
                return goaldiceroll + 6
            elif theirscore-myscore >= 50:
                return goaldiceroll + 5
            elif theirscore-myscore >= 40:
                return goaldiceroll + 4
            elif theirscore-myscore >= 30:
                return goaldiceroll + 3
            elif theirscore-myscore >= 20:
                return goaldiceroll + 2
            elif theirscore-myscore >= 10:
                return goaldiceroll + 1
            else:
                return goaldiceroll 
        else: #My score is greater than theirs
            return 0
    else: #If they've NOT quit yet
        if theirscore > myscore: #If their score is larger than mine 
            if myscore >= 90: #RECONSIDER
                return 1
            elif myscore >= 80:
                return goaldiceroll
            elif myscore >= 70: #RECONSIDER
                return goaldiceroll
            elif myscore >= 60:
                return goaldiceroll
            elif myscore >= 50: #RECONSIDER
                return goaldiceroll
            elif myscore >= 40:
                return goaldiceroll
            elif myscore >= 30: #RECONSIDER
                return goaldiceroll
            elif myscore >= 20:
                return goaldiceroll
            else: #Less than 20
                return goaldiceroll +1
        elif theirscore == myscore: #If their score is the exact same as mine
            if myscore >= 90:
                return 0
            elif myscore >= 80:
                return 1
            elif myscore >= 70:
                return goaldiceroll
            elif myscore >= 60:
                return goaldiceroll
            elif myscore >= 50:
                return goaldiceroll
            elif myscore >= 40:
                return goaldiceroll
            elif myscore >= 30:
                return goaldiceroll
            elif myscore >= 20:
                return goaldiceroll
            elif myscore >= 10:
                return goaldiceroll
            else:
                return goaldiceroll +1
        elif theirscore < myscore:#If their score is less than mine
            if myscore >= 90:
                return 0
            elif myscore >= 80:
                return (-1*(goaldiceroll -1))//2
            elif myscore >= 70:
                return (-1*goaldiceroll)//2
            elif myscore >= 60:
                return (-1*goaldiceroll)//2
            elif myscore >= 50:
                return (-1*goaldiceroll)//2
            elif myscore >= 40:
                return (-1*goaldiceroll)//2
            elif myscore >= 30:
                return (-1*goaldiceroll)//2
            elif myscore >= 20:
                return (-1*goaldiceroll)//2
            elif myscore >= 10:
                return (-1*goaldiceroll)//2
            else:
                return (-1*(goaldiceroll +1))//2
        else: 
            return 0 #0 because something went wrong
def thisoneatleastwins4times(myscore,theirscore,last):
    #Get the mean of myscore - theirscore, roll whatever dice you need to try and get that
    if myscore >theirscore:
        goaldiceroll = (-1 * int((myscore-theirscore)//3.5))-1
    elif myscore<theirscore:
        goaldiceroll = int((theirscore-myscore)//3.5) +1
    else:
        goaldiceroll =1


    if last == True: #if it's the last turn
        if theirscore > myscore:    
            return goaldiceroll +3
        elif theirscore == myscore: 
            return 1
        else: #My score is greater than theirs
            return 0            
    else: #If they've NOT quit yet
        if theirscore > myscore: #If their score is larger than mine 
            return goaldiceroll
        elif theirscore == myscore: #If their score is the exact same as mine
            return 1
        elif theirscore < myscore:#If their score is less than mine
            return (-1*(goaldiceroll//2))
        else: 
            return 0 #0 because something went wrong #Up to this point, the tests were not successful. This one however, consistently beat tests 1-4
def coppertest(myscore,theirscore,last): #Tried playing around with dividing by different values/adverages.

    if myscore > theirscore:
        goaldiceroll = int(-1 * abs((theirscore-myscore)/3.5))
    elif myscore < theirscore:
        goaldiceroll = int(abs((theirscore-myscore)/3.5))
    else:
        if myscore >= 100:
            goaldiceroll = 0
        elif myscore >= 95:
            goaldiceroll = 2
        elif myscore >= 90:
            goaldiceroll = 3
        elif myscore >= 85:
            goaldiceroll = 5
        elif myscore >= 80:
            goaldiceroll = 7
        elif myscore >= 70:
            goaldiceroll = 10
        elif myscore >= 60:
            goaldiceroll = 12
        elif myscore >= 50:
            goaldiceroll = 15
        elif myscore >= 40:
            goaldiceroll = 17
        elif myscore >= 30:
            goaldiceroll = 20
        else:
            goaldiceroll = 25

    if myscore ==0: #First turn for me
        if theirscore >0: #go second
            return int((theirscore/4.5) +3)
        else: #go first
            return 32

    elif last == True: #if it's the last turn
        if theirscore > myscore: 
            if myscore >= 97:
                return 1
            elif myscore >= 90:
                return 2
            else: 
                return goaldiceroll +3
        elif theirscore == myscore: 
            return 1
        else: #My score is greater than theirs
            return 0  

    else: #If they've NOT quit yet
        if theirscore > myscore: #If their score is larger than mine 
            if myscore >= 100: 
                return 0
            elif myscore >= 95:
                return 1
            elif myscore >= 90:
                return 2
            elif myscore >= 85:
                return goaldiceroll
            elif myscore >= 80:
                return goaldiceroll +1
            elif myscore >= 70:
                return goaldiceroll +2
            elif myscore >= 10:
                return goaldiceroll + (goaldiceroll//2)
            else: #Less than 20
                return goaldiceroll +10
        elif theirscore == myscore: #If their score is the exact same as mine
            if myscore >= 100: 
                return 0
            elif myscore >= 95:
                return 1
            elif myscore >= 90:
                return goaldiceroll
            elif myscore >= 85:
                return goaldiceroll +2
            elif myscore >= 80:
                return goaldiceroll +3
            elif myscore >= 70:
                return goaldiceroll +4
            elif myscore >= 10:
                return goaldiceroll +5
            else:
                return goaldiceroll +10
        elif theirscore < myscore: #If their score is less than mine
            if myscore >= 100: 
                return 0
            elif myscore >= 95:
                return 0
            elif myscore >= 90:
                return goaldiceroll
            elif myscore >= 85:
                return goaldiceroll +1
            elif myscore >= 80:
                return goaldiceroll +2
            elif myscore >= 70:
                return goaldiceroll +3
            elif myscore >= 10:
                return goaldiceroll +4
            else:
                return goaldiceroll +10
        else: 
            return 0 #0 because something went wrong

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
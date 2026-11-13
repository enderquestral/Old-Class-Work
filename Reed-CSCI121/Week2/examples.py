def square(x):
    return x * x

def successor(n):
    return n + 1

def distanceFromTo(startX, startY, endX, endY):
    changeX = endX - startX
    changeY = endY - startY
    distanceSquared = (changeX ** 2) + (changeY ** 2)
    return distanceSquared ** 0.5

def gains(initial, yearly_rate, years):
    multiplier = 1.0 + yearly_rate / 100.0
    growth = multiplier ** years 
    amount = initial * growth
    return amount - initial

def absoluteValue(x):
    if x >= 0:
        return x
    else:
        return -x

def sumOfSquaresTo(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + square(i)
        i = i + 1
    return sum

def printBoxTop(size):
    dashes = "-" * size
    print("+" + dashes + "+")

def printBox(boxWidth):
    printBoxTop(boxWidth)
    print("|" + (" " * boxWidth) + "|")
    printBoxTop(boxWidth)

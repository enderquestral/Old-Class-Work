#partner: hanheller
#partner: garciase
def sum_cubes(n):
    sum = 0
    while n > 0:
        sum = sum + (n ** 3) 
        n = n - 1 
    return sum
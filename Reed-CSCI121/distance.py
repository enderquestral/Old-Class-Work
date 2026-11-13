locx = float(input("Location x-coordinate? "))
locy = float(input("Location y-coordinate? "))
classx = float(input("Classroom x-coordinate? "))
classy = float(input("Classroom y-coordinate? "))

print( (((classx-locx)**2) + (classy - locy)**2) **0.5 )
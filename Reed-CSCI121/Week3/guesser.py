import random
print("I've just chosen a number from 1 to 100.")
print("Let's see if you can guess what it is!" + "\n" + "\n")
number = random.randint(1,101)




guess = int(input("What's your first guess? "))
guesses = 1

while guesses <= 6 and guess != number:
    if guess < number:
        print("That's too low!")
    else: 
        print("That's too high, try again!")
    guess = int(input("Enter another guess: "))
    guesses = guesses +1

if guess == number:
    print("Nice job! You seemed to read my mind! Wow")
else:
    print("Whoops, tough luck sucker.")
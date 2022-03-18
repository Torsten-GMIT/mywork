# Author: Torsten Kindt
# working on lab sheet 4.1

# Modify the program from guess1.py so that it tells the user if their guess is too high or too low. Use an if-statement inside the while loop.

# while condition:
    # statement   <-- using the if-statement here

# 1. Initialise condition variables
# 2. Check condition
# 3. Change condition variables


num = int(input("Guess a number between 1 and 10: "))
while num != 6:
    if num > 6:
        print("Your guess is too high:", num,'. Guess again.')

    elif num < 6:
        print("Your guess",num,"is too low. Guess again.")
    
    num = int(input("You were wrong! Guess again: "))
    
print("Well done indeed. Yes, the number was 6.")


# getting error and program stops when accidentially pushing empty enter button (no input) or entering anything else than an int. Why?
# ValueError: invalid literal for int() with base 10: ''

# "Empty" or float are no int, still should this happen? How to avoid? 


# same with the solution

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)

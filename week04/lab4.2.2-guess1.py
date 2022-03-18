# Author: Torsten Kindt
# working on lab sheet 4.1

# Write a program that prompts a user to guess a number until the user gets it right.

# while condition:
    # statement

# 1. Initialise condition variables
# 2. Check condition
# 3. Change condition variables


num = input("Guess a number between 0 and 10: ")
while num != "2":
    print("You guessed wrong: " + num + ". Guess again.")
    num = input("You were wrong! Guess again: ")
print("Well done! Yes, the number was 2.")

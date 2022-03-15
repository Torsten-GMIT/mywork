# Author: Torsten Kindt
# working on lab sheet 2.2 (before watching lecture)

# small program adding 1 to a number input and prints the sum

yourNumber = input("Enter your number here: ")
answer = int(yourNumber) + 1
print(answer)

# output adjusted after watching lecture
# input returns a string, input must be converted to integer

yourNumber = int(input("Enter your number here: "))
answer = yourNumber + 1
print("Your number {} plus one is {}".format(yourNumber, answer))




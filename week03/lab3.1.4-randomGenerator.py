# Author: Torsten Kindt
# working on lab sheet 3.1

# a program that prints a random number between 1 and 10
# importing modules

# input returns a string, needs to be converted to int to do mathematic calculations


import random

number = random.randint(1, 10)
print("Here is a random number {}".format(number))


# try modifying the program so that the user inputs the range

num1 = int(input("Enter your first number of your chosen range: "))
num2 = int(input("Enter your second number of yoru chosen range: "))

number = random.randint(num1, num2)
print("Here is a random number from your chosen range: {}".format(number))
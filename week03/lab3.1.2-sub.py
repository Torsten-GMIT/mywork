# Author: Torsten Kindt
# working on lab sheet 3.1

# a program that reads in two numbers and subtracts the first from the second
# input returns a string, needs to be converted to int

num1 = int(input("Enter your first number here: "))
num2 = int(input("Enter your second number here: "))
answer = num1 - num2
print("{} minus {} is {}".format(num1, num2, answer))


# The print command is set in double quotes = string. Hence adding more strings, e.g. Hello, won't matter. 
 
print("Hello, your first number {} minus your second number {} is {}".format(num1, num2, answer))

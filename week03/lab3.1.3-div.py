# Author: Torsten Kindt
# working on lab sheet 3.1

# a program that reads in two numbers and divides the first by the second to output the result as integer with the remainder

# input returns a string, needs to be converted to int to do mathematic calculations

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter the number you want to divide by: "))
answer = int(num1/num2)  # converting to int not to give you a float
rest = (num1%num2)

print("{} divided by {} is {} with a remainder of {}".format(num1, num2, answer, rest))
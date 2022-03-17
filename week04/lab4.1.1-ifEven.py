# Author: Torsten Kindt
# working on lab sheet 4.1

# Write a program that reads in a number and then the user if the number is even or odd.

# input returns a string, getting error msg, converting input to number

num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
# Author: Torsten Kindt
# working on lab sheet 3.2

# write a program that reads in a number (as a float) and outputs an integer rounded down (i.e., its mathematic floor)

# I have to import the python math module for the mathematic floor function because it is not a built-in function


import math
    #print(dir(math))    ## to find function to use
from math import floor

num1 = float(input("Enter a floating-point number: "))
print("{} floored is {}".format(num1, floor(num1)))

# as per https://docs.python.org/3.9/library/math.html?highlight=floor#math.floor and https://www.w3schools.com/python/python_modules.asp


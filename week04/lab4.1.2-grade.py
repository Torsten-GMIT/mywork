# Author: Torsten Kindt
# working on lab sheet 4.1

# Write a program that reads in a student's percentage mark and prints out the corresponding grade.

# Percentage can be a float, so converting input str into float

# Task asks for "Between 40% and 49%" not just (>40%)?

# The defined task leaves gaps which produce always "Distinction" because "else", e.g. any percentage over x9. For instance 49.5 gets a Distinction when it should be a Pass.

# I think, for this program to work, if-values should be up to x9.9 to close the gap?


percentage = float(input("Enter student's percentage here: "))

if percentage < 40:
    print("Fail")
elif (percentage >= 40) and (percentage <= 49.9):
    print("Pass")
elif (percentage >= 50) and (percentage <= 59):
    print("Merit 2")
elif (percentage >= 60) and (percentage <= 69):
    print("Merit 1")
else:
    print("Distinction")

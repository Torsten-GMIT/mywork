# Author: Torsten Kindt
# working on lab sheet 4.1

# How to round the percentages from lab 4.1.2?

percentage = round(float(input("Enter student's percentage here: "))) 
# I just took a guess, it worked :)
# All those brackets are confusing, though. Have to get used to the logic behind it.


if percentage < 40:
    print("Fail")
elif (percentage >= 40) and (percentage <= 49):
    print("Pass")
elif (percentage >= 50) and (percentage <= 59):
    print("Merit 2")
elif (percentage >= 60) and (percentage <= 69):
    print("Merit 1")
else:
    print("Distinction")
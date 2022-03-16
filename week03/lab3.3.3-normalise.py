# Author: Torsten Kindt
# working on lab sheet 3.3

# Write a program that reads in a string and strips any leading or trailing spaces, and converts the string to all lower cases.
# Also output should tell the length of input and length of output strings

origString = input("Enter a string: ")
stringStripped = origString.strip()

print("That string normalised is: {}\nWe reduced the input string from {} to {} characters.".format(stringStripped.lower(), len(origString), len(stringStripped)))

# https://www.w3schools.com/python/ref_string_strip.asp
# https://www.w3schools.com/python/ref_string_lower.asp
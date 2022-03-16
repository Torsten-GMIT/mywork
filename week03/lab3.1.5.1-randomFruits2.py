# Author: Torsten Kindt
# working on lab sheet 3.1

# write a program that prints out a random fruit
# use tuple () instead of list []


import random

fruits = ("Apple", "Orange", "Banana", "Pear")
print("Here is a random fruit: {}".format(random.choice(fruits)))  


# solution taken from stackoverflow and adjusted, https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list

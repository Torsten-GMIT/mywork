# Author: Torsten Kindt
# working along with lecture 4.2
# learning about loops

# while condition:
    # statement

# 1. Initialise condition variables
# 2. Check condition
# 3. Change condition variables

# variable rules apply, e.g. naming


# Counter controlled loop

count = 0
while count < 10:
    print(count)
    count += 1

print()

whatever = 0
while whatever < 10:
    print(whatever)
    whatever += 1

print()

count = 10
while count >= 0:
    print(count)
    count -= 1


# Sentinal controlled loop

val = input("Enter something (q to quit):")
while val != "q":
    print("You wrote: " + val)
    val = input("(q to quit):")
print("goodbye")



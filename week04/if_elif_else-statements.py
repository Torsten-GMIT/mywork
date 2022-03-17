# Author: Torsten Kindt
# working along with lecture 4.1
# learning about statements - if, elif, else

b = 2
if b == 2:
    print("b is equal to 2.")
else:
    print("b is not equal to 2.")

a = 2
if a != 2:
    print("I hope this is not displayed!")
else:
    print("2 is not equal to 2 is false.")


aNumber = 5
if (aNumber % 2) == 0:  # brackets for clarity of operation
    print(aNumber, "is even.") # another way of printing variables without .format() - separated by comma

elif aNumber % 3 == 0:  # works without brackets, too
    print(aNumber, "is divisable by 3.")

else:
    print(aNumber, "is not even or divisable by 3.")

print("\nThis will always be outputted.")

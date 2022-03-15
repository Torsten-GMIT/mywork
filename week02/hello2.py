# Author: Torsten Kindt
# working on lab sheet 2.2

# Print "Hello + an input name"
# input window pops up

name = input("Enter your name here:")
print("Hello " + name)

# modify to say  Nice to meet you

name = input("Enter your name here:")
print("Hello " + name + "\nNice to meet you.")

# not: \n = line break, space after Hello inside "" no other spaces are printed

# or you could say this with format

name = input("Enter your name here:")
print("Hello {}\nNice to meet you." .format(name))





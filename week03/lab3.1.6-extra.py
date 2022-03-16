# Author: Torsten Kindt
# working on lab sheet 3.1

# Questions

# 6. Why does this expression cause an error?

    # message = "I have eaten " + 99 + " burritos."
    # print(message)

# Answer: message mixes strings with integer. Python can't concatenate.
# My fix: converting the whole message into a string

message = ("I have eaten 99 burritos.")
print(message)

# 7. Why is eggs a valid name while 100 is invalid? 

# Answer: Python does not allow numbers as names for variables. Variable names must start with a letter. 

# 8. What three functions can be used to get the integer, floating-point number, or string versing of a value?

# Answer: int(), float(), str()
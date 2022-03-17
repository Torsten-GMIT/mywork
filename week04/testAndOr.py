# Author: Torsten Kindt
# working along with lecture 4.1
# learning about variable types - ands and ors

number = 77
if (number >= 0) and (number <= 100):  # brackets for clarity!
    print("valid")

num = -7
if (num <= 0) or (num >= 100): 
    print("stop")
    # 'if' tests for true - if (true) or if (true): then (print). 
    # 'and' instead of 'or' will produce error because both statements can't be true. 

else:
    print("go")
#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
operator = number % 10 if number > 10 else number % -10
print (f"last digit of {number} is {operator}")
if operator > 5:
    print("greater than 5")
elif operator == 0:
    print("0")
else:
    print("less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit =abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
operator = "lastdigit of {} is {}.format (number, lastdigit)"
print (f"last digit of {number} is {operator}")
if lastdigit > 5:
    print(f"{operator}greater than 5")
elif lastdigit == 0:
    print(f"{operator} and is 0")
elif lastdigit < 6:
    print(f"{operator} and less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = number
number00 = 0
if number < 0:
    number00 = number % -10
else:
    number00 = number % 10
if number00 > 5:
    print(f"Last digit of {number1} is {number00} and is greater than 5")
elif (number00 < 6) and (number00 != 0):
    print(f"Last digit of {number1} is {number00} and is less than 6 and not 0")
elif number00 == 0:
    print(f"{number00} is zero")

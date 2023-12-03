#!/usr/bin/python3
import random
number0 = random.randint(-10000, 10000)
number1 = number0
number = 0
if number0 < 0:
    number = number0 % -10
else:
    number = number0 % 10
if number > 5:
    print(f"Last digit of {number1} is {number} and is greater than 5")
elif (number < 6) and (number != 0):
    print(f"Last digit of {number1} is {number} and is less than 6 and not 0")
elif number == 0:
    print(f"{number} is zero")

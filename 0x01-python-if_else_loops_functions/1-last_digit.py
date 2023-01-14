#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# checking if number is positive or negative
if number > 0:
    lastdigit = number % 10
elif number < 0:
    # convert number to positive
    number = (number * -1)
    lastdigit = number % 10
    # convert the result to negative
    lastdigit = (lastdigit * -1)
    # convert number to its original state i.e negative
    number *= -1
    # checking if number is 0 then the last digit is 0
elif number == 0:
    lastdigit = 0

if lastdigit > 5:
    print("Last digit of {} is {} and is \
greater than 5".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastdigit))
elif lastdigit != 0 and lastdigit < 6:
    print("Last digit of {} is {} and is less than \
6 and not 0".format(number, lastdigit))

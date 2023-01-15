#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        lastdigit = number % 10
        print(lastdigit, end="")
    elif number == 0:
        lastdigit = 0
        print(lastdigit, end="")
    elif number < 0:
        number *= -1
        lastdigit = number % 10
        print(lastdigit, end="")
    return lastdigit

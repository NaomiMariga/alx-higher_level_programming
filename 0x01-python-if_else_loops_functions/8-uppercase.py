#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        number = ord(letter)
        if number >= 97 and number <= 122:
            letter = number - 32
            letter = chr(letter)
            print("{}".format(letter), end="")
        else:
            letter = chr(number)
            print("{}".format(letter), end="")

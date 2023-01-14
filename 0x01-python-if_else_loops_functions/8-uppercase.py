#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for letter in str:
        number = ord(letter)
        if number >= 97 and number <= 122:
            letter = number - 32
            letter = chr(letter)
            new_str += letter
        else:
            letter = chr(number)
            new_str += letter
    print("{}".format(new_str))

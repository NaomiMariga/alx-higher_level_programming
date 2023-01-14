#!/usr/bin/python3
for i in range(0, 10):
    for k in range(0, i):
        if k < i:
            if str(i) + str(k) != str(k) + str(i):
                print("{}{}, ".format(k, i), end="")

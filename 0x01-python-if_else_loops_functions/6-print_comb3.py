#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if ((str(i) + str(j)) != str(j) + (str(i))):
            if (str(i) + str(j) != str(89)):
                print("{}{}, ".format(i, j), end="")
            else:
                print("{}{}".format(i, j))

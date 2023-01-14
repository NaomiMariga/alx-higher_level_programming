#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        # 02d implements a minimum of width 2, hence 01 instead of 1
        print("{:02d}, ".format(i), end="")
print(i)

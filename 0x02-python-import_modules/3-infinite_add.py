#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    number = len(argv)
    sum = 0

    for i in range(number):
        sum += int(argv[i])

    print(sum)

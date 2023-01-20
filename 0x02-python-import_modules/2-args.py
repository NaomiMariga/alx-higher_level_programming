#!/usr/bin/python3
def print_args(arguments):
    number = len(arguments)

    if number == 0:
        print("{} arguments.".format(number))
    elif number == 1:
        print("{} argument:".format(number))
        print("{}: {}".format(number, arguments[0]))
    else:
        print("{} arguments:".format(number))
        for argument in range(number):
            print("{}: {}".format(argument + 1, arguments[argument]))


if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    print_args(argv)

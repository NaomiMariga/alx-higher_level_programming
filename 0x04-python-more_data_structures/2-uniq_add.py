#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = set(my_list)
    sum = 0
    for i in uniques:
        sum += i

    return sum

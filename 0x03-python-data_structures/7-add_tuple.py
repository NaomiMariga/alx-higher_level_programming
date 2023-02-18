#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    addition = []
    sum = 0

    if len(tuple_a) == 1:
        a = list(tuple_a)
        a.append(0)
        tuple_a = tuple(a)
    elif len(tuple_b) == 1:
        b = list(tuple_b)
        b.append(0)
        tuple_b = tuple(b)
    elif len(tuple_b) < 1:
        b = list(tuple_b)
        b.append(0)
        b.append(0)
        tuple_b = tuple(b)
    elif len(tuple_a) < 1:
        a = list(tuple_a)
        a.append(0)
        a.append(0)
        tuple_a = tuple(a)

    for i in range(len(tuple_a[0:2])):
        sum = tuple_a[i] + tuple_b[i]
        addition.append(sum)

    tuple_addition = tuple(addition)
    return tuple_addition

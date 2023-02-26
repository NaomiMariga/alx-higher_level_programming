#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    results = {}
    for key, value in a_dictionary.items():
        prod = value * 2
        results.update({key: prod})
    return results

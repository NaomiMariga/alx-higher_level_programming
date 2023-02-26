#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    results = {}
    for key, value in a_dictionary.items():
        if value % 2 == 0:
            results.update({key: value})
    return results

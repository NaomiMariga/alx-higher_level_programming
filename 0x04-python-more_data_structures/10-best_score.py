#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != {} and a_dictionary is not None:
        values = []
        keys = []
        for key, value in a_dictionary.items():
            values.append(value)
            keys.append(key)
        maxnum = max(values)
        maxnum_pos = values.index(maxnum)
        key = keys[maxnum_pos]
        return key
    else:
        return None

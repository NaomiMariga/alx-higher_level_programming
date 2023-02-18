#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        result = tuple((len(sentence), sentence[0]))
        return result
    else:
        result = tuple((len(sentence), None))
        return result

#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """returns length of string of a tuple"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

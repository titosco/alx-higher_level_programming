#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """func finds the bigest num"""
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > biggest:
            biggest = my_list[i]

    return (biggest)

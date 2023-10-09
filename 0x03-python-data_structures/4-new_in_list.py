#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """replace element without modifying said list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    original = [x for x in my_list]
    original[idx] = element
    return (original)

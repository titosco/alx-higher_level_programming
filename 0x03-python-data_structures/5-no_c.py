#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """remove c and C from sting"""
    paste = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(paste))

#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    counts = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counts += 1
        except (ValueError, TypeError):
            pass
    print()
    return counts

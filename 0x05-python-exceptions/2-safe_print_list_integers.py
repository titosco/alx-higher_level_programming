#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    counting = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counting += 1
        except (ValueError, TypeError):
            pass
        print()
        return counting

#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    counting = 0
<<<<<<< HEAD
    for i in range(0, x):
=======
    for i in range(x):
>>>>>>> 950e41079db3aa42559f2d5c2a8706c6adca37f1
        try:
            print("{:d}".format(my_list[i]), end="")
            counting += 1
        except (ValueError, TypeError):
            pass
        print()
        return counting

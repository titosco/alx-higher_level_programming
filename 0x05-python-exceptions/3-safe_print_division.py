#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    try:
        divd = a/b
    except (ZeroDivisionError):
        divd = None
    finally:
        print("inside result: {}".format(divd))
        return divd

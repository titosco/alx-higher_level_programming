#!/usr/bin/python3
# 100-safe_print_integer_err.py

def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True

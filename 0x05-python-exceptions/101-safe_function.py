#!/usr/bin/python3
# 101-safe_function.py

def safe_function(fct, *args):
    import sys

    try:
        numb = fct(*args)
        return numb
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None

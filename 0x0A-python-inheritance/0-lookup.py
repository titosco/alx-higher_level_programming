#!/usr/bin/python3
# 0-lookup.py
"""Define an object attributes lookup function"""


def lookup(obj):
    """
    look ups at obj attributes and methods.
    Args:
            obj to list.
    Returns lists pof attributes.
    """

    return dir(obj)

#!/usr/bin/python3
# 4-inherits_from.py
"""module for inherets_from method"""


def inherits_from(obj, a_class):
    """see if obj is true subclass of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class

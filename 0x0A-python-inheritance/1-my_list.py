#!/usr/bin/python3
# 1-my_list.py
"""inhereted module from my class"""


class MyList(list):
    """Custom MyList class"""

    def print_sorted(self):
        """Method for printing my class"""
        print(sorted(self))

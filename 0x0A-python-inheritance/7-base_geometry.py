#!/usr/bin/python3
# 7-base_geometry.py
"""module for base_geometry"""


class BaseGeometry:
    """a class basegeometry"""

    def area(self):
        """method to compute area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method to vcalidate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

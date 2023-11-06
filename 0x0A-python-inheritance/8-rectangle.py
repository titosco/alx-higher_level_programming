#!/usr/bin/python3
# 8-rectangle.py
"""module for rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass representing rectangle"""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height

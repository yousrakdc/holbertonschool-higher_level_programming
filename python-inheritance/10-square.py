#!/usr/bin/python3

"""import BaseGeometry"""

Rectangle = __import__('9-base_geometry').Rectangle


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, size):
        """ initializes square """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

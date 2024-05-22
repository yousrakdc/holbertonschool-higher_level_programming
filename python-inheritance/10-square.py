#!/usr/bin/python3

"""import BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialization width and height of rectangle"""
        self.integer_validator("size", size)
        self.__init__(size, size)
        self.__size = size

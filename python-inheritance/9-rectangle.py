#!/usr/bin/python3

"""import BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialization width and height of rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def __str__(self):
        """str"""
        a = str(self.__width)
        b = str(self.__height)
        return "[" + __class__.__name__ + "] " \
            + a + "/" + b

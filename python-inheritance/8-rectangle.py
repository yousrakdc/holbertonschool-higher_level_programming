#!/usr/bin/python3

"""class BaseGeometry"""


class BaseGeometry:
    """not so empty class"""
    def area(self):
        """area implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer """
        if type(value) is not (int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialization width and height of rectangle"""
        self().integer_validator("width", width)
        self().integer_validator("height", height)
        self.__width = width
        self.__height = height

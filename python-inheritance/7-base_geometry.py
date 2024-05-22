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

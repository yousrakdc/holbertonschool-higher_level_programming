#!/usr/bin/python3
"""Class Square that defines a square"""


class Square():
    "Define a private size attribute"
    def __init__(self, size=0):
        "Square initialization"
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

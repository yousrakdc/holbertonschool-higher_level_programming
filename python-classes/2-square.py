#!/usr/bin/python3
"""Class Square that defines a square"""


class Square():
    "Define a private size attribute"
    def __init__(self, size=0):
        "Square initialization"
        self.__size = size

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    pass

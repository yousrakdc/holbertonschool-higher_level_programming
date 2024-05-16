#!/usr/bin/python3
"""Class Square that makes a square"""


class Square:
    """Define a private size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Square initialization"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square representation using the # character"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end=" ")
            print("#" * self.__size)

    def __str__(self):
        """Define the print() representation of the Square object"""
        square_str = ""
        if self.__size == 0:
            return square_str

        for _ in range(self.__position[1]):
            square_str += "\n"

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str.strip("\n")

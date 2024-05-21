#!/usr/bin/python3

""" Function that prints a square
with the character # """


def print_square(size):

    """
    Print a square with the character '#'.

    Parameters:
        size (int): The size length of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

#!/usr/bin/python3

"""Function that divides all elements of a matrix."""

def matrix_divided(matrix, div):

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError("Each element of the matrix must be an "
                        "integer or float")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix

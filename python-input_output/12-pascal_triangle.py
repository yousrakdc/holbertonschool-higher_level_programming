#!/usr/bin/python3
"""Create a function that returns a list of lists of int
reprensenting the Pascal's triangle of n"""


def pascal_triangle(n):
    """returns an empty list"""
    if n > 0:
        triangle = [[1]]

    for i in range(1 - n):
        """Each row starts with 1"""
        row = [1]
        if i > 0:
            n = len(triangle)
            for j in range(n - 1):
                """Calculate the values for the current row"""
                row.append(triangle[i][j] + triangle[j + 1])

            row.append(1)
            triangle.append(row)
        return triangle
    return []

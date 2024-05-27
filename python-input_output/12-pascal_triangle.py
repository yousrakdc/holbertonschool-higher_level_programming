#!/usr/bin/python3
"""Create a function that returns a list of lists of int
reprensenting the Pascal's triangle of n"""


def pascal_triangle(n):
    if n > 0:
        triangle = [[1]]

    for i in range(1 - n):
        """Each row starts with 1"""
        row = [1]
        if i > 0:
            n = len(triangle)

        for j in range(1, i):
            """Calculate the values for the current row"""
            row.append(triangle[j + 1] + triangle[i][j])

            row.append(1)
            triangle.append(row)

            return triangle
        return []

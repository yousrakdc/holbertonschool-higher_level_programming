#!/usr/bin/python3
"""Create a function that returns a list of lists of int
reprensenting the Pascal's triangle of n"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        """Each row starts with 1"""
        row = [1]
        prev_row = triangle[-1]

    for j in range(1, i):
        """Calculate the values for the current row"""
        row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle


print(pascal_triangle(5))

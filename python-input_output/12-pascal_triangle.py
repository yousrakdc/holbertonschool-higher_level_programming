#!/usr/bin/python3
"""Create a function that returns a list of lists of int
reprensenting the Pascal's triangle of n"""


def pascal_triangle(n):
    triangle = list()

    if n <= 0:
        return triangle

    if n > 0:
        triangle.append([1])

    # Add second line.
    if n > 1:
        triangle.append([1, 1])

    for x in range(3, n+1):
        triangle.append([0] * x)

        # Set first and last 1
        triangle[x-1][0] = 1
        triangle[x-1][x-1] = 1

        # Calculate middle numbers
        for y in range(1, x-1):
            triangle[x-1][y] = \
                triangle[x-2][y-1] + triangle[x-2][y]

    return triangle
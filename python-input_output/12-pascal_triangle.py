#!/usr/bin/python3
"""Create a function that returns a list of lists of int
reprensenting the Pascal's triangle of n"""


def pascal_triangle(n):
    """function to find Pascal's Triangle integers"""
    if n > 0:
        triangle = [[1]]
        for i in range(n - 1):
            my_list = [1]
            if i > 0:
                n = len(triangle)
                for j in range(n - 1):
                    my_list.append(triangle[i][j] + triangle[i][j + 1])
            my_list.append(1)
            triangle.append(my_list)
        return triangle
    return []

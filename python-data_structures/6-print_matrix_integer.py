#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
        return

    for row in matrix:
        row_str = ""
        for num in row:
            row_str += "{:d} ".format(num)
        print(row_str.rstrip())

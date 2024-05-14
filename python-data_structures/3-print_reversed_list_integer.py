#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for integer in reversed(my_list):
        print(str.format("{:d}", integer))

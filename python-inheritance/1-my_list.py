#!/usr/bin/python3

"""Write a class MyList that inherits from list"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """prints list"""
        print(sorted(self))

#!/usr/bin/python3

"""function that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """look for attributes"""
    return [method for method in dir(obj)]

#!/usr/bin/python3

"""function that appends a string at the end of a text file (UTF8)
returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends file"""
    with open(filename, 'a', encoding="UTF-8") as f:
        f.write(text)
    return len(text)

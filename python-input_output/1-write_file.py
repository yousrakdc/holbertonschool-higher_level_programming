#!/usr/bin/python3

"""function that writes a string to a text file (UTF8)
returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes file"""
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(text)
    return len(text)

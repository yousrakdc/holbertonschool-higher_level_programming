#!/usr/bin/python3

"""function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    with open(filename, mode='r', encoding="UTF8") as file:
        print(file.read())

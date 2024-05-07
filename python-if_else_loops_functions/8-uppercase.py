#!/usr/bin/python3
def uppercase(str):

    uppercase_chars = []

    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char

        uppercase_chars.append(uppercase_char)

    uppercase_str = ''.join(uppercase_chars)
    print("{}".format(uppercase_str))

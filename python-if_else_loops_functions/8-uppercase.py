#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:

        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:

            uppercase_char = char

        uppercase_str += uppercase_char

    print(uppercase_str)


uppercase("best")

uppercase("best school 98 battery street")

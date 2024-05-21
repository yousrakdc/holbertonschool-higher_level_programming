#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Print the provided first and last name
    (if provided) in a formatted string.

    Parameters:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed.
        Defaults to an empty string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is", first_name)

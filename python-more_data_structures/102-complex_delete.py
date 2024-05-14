#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict(a_dictionary)

    for key, val in a_dictionary.items():

        if val == value:
            del new_dict[key]

    return new_dict

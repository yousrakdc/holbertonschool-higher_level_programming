#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del a_dictionary[key]


my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
complex_delete(my_dictionary, 2)
print(my_dictionary)

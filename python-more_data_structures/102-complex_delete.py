#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dictionary_copy = a_dictionary.copy()


    for key, val in dictionary_copy.items():
         if val == value:
             del a_dictionary[key]

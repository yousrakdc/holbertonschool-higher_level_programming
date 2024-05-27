#!/usr/bin/python3
""" function that returns the dictionary description with simple data structure
for JSON serialization of an object:"""


def class_to_json(obj):
    attributes = {}

    for attr_name in dir(obj):
        if not attr_name.startswith('___'):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                attributes[attr_name] = attr_value
    return attributes

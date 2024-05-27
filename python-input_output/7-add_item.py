#!/usr/bin/python3
"""Script that adds all arguments to a Python list
and then saves them to a file"""

import json
import sys
import os


def save_to_json_file(my_obj, filename):
    """Save the JSON string representation of object to file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Load from JSON"""
    with open(filename, 'r') as file:
        return json.load(file)


try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, "add_item.json")

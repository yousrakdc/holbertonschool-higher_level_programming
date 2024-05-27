#!/usr/bin/python3
"""function to save string to file"""
import json


def save_to_json_file(my_obj, filename):
    """Save the JSON string representation of object to file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

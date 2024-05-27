#!/usr/bin/python3
"""Function that writes an Object to a text file using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Writes the JSON string representation of my_obj
    to a file specified by filename.

    Args:
        my_obj: The object to be serialized into JSON and written to the file.
        filename: The name of the file to write the JSON string to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

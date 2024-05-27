#!/usr/bin/python3
"""Script that adds all arguments to a Python list
and then saves them to a file"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, "add_item.json")

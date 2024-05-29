#!/usr/bin/env python3
"""Serialize and deserialize data"""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """deserialize"""
    with open(filename, 'r') as file:
        return json.load(file)

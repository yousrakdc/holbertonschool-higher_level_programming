#!/usr/bin/env python3
"""Serialize and deserialize data"""

import pickle


def serialize_and_save_to_file(data, filename):
    """serialize and save"""
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """deserialize"""
    with open(filename, 'rb') as file:
        deserialized_data = pickle.load(file)
    return deserialized_data

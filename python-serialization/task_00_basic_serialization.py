#/usr/bin/env python3
"""Serialize and deserialize data"""

import pickle

def serialize_and_save_to_file(data, filename):
    with open('filename', 'wb') as file:
        pickle.dump(data, file)
        print(f"Data serialized and saved to {filename}")

def load_and_deserialize(filename):
    with open(filename, 'rb') as file:
        deserialized_data = pickle.load(file)
        print("Deserialized Data:")
        print(deserialized_data)

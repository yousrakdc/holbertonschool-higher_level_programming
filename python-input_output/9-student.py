#!/usr/bin/python3
"""Write a class Student that defines a student"""

import json


class Student:
    """Initializes a Student instance with first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self):
    """Retrieves a dictionary representation of a Student instance."""
    return {
        "first_name": self.first_name,
        "last_name": self.last_name,
        "age": self.age
    }

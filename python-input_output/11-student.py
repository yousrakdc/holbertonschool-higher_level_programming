#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """student class"""
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {
                val: value
                for val, value in self.__dict__.items()
                if val in attrs
            }

    def reload_from_json(self, json):
        """change attributes"""
        for attr, value in json.items():
            setattr(self, attr, value)

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

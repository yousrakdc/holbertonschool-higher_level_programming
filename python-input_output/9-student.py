#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """student class"""
    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__

    def __init__(self, first_name, last_name, age):
        """Initializes Student instance with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

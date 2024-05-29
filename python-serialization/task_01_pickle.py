#!/usr/bin/env python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:

    def serialize(self, filename):
        """serialize"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserialize"""
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                return data
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None

    def __init__(self, name, age, is_student):
        """initialization"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

#!/usr/bin/python3

"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """animal class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """subclass dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass: Cat"""
    def sound(self):
        return "Meow"

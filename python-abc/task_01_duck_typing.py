#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""Shapes, Interfaces, and Duck Typing"""

class Shape(ABC):
    """define shape"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """implements the area and perimeter methods"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Create the Rectangle class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Define the shape_info function"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

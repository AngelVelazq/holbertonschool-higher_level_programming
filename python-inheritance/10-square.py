#!/usr/bin/python3
"""This module contains the definition of the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance with size"""
        self.integer_validator("size, size")
        self.__ = size
        super().__init__(size, size)

    def area(self):
        """area method implemented"""
        return self.__ ** 2

#!/usr/bin/python3
"""This module defines a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2

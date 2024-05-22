#!/usr/bin/python3
"""This module contains the definition of the Rectangle class."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

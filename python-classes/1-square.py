#!/usr/bin/env python3
"""square module

This module provides a class to represent a square with a private
instance attribute for its size."""


class Square:
    """A class used to represent a Square."""

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
        size : int
            The size of the square
        """
        self.__size = size

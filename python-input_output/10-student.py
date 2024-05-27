#!/usr/bin/python3
"""This module defines a class Student that defines a student by
public instance attributes first_name, last_name, and age."""


class Student:
    """Student - A class that defines a student

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student"""

    def __init__(self, first_name, last_name, age):
        """__init__ - Initializes the student instance with attributes

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: A list of strings representing the attributes to retrieve.

        Returns:
            dict: A dictionary representation of the instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student."""

    def __init__(self, first_name, last_name, age):
        """Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json - Retrieves a dictionary

        Returns:
            dict: A dictionary representation of the instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """reload_from_json - Replaces all attributes Student instance."""
        for key, value in json.items():
            setattr(self, key, value)

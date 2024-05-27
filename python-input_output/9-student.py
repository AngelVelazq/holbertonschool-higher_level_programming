#!/usr/bin/python3
"""This module defines a class Student that defines a student by
public instance attributes first_name, last_name, and age."""


class Student:
    """Defines a student with attributes first_name, last_name,
    and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json - Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the instance.
        """
        return self.__dict__

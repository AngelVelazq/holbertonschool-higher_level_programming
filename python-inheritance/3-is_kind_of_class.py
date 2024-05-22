#!/usr/bin/python3
"""This module contains the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance, or if the object is an instance
    of a class that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, False if not
    """
    return isinstance(obj, a_class)

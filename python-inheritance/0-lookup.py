#!/usr/bin/python3
"""
This module contains the function `lookup` which returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.
Returns:
        A list of attributes and methods of the object."""
    return dir(obj)

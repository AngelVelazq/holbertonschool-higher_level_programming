#!/usr/bin/python3
"""
0-add_integer.py

This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers and return result. If b not provided, it defaults to 98.

    Both a and b must be integers or floats, otherwise a TypeError is raised.
    Floats are typecast to integers before addition.

    Args:
        a: The first number.
        b: The second number (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.

    Examples:
    >>> add_integer(2, 3)
    5
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(2.5, 2.5)
    4
    >>> add_integer("2", 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(2, "3")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    if isinstance(a, bool):
        raise TypeError('a must be an integer')
    if isinstance(b, bool):
        raise TypeError('b must be an integer')
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)
    return a + b

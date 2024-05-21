#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the maximum integer in a list of integers.
       If the list is empty, the function returns None.
    """
    if not all(isinstance(x, (int, float)) for x in list):
        raise TypeError("list must contain only integers or floats")
    if len(list) == 0:
        return None
    result = list[0]
    for i in list:
        if i > result:
            result = i
    return result

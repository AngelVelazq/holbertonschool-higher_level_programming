#!/usr/bin/python3
"""This module defines a function to write an Object to
a text file using a JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - Writes an Object to a text file using a JSON
    representation.

    Args:
        my_obj: The object to be serialized.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

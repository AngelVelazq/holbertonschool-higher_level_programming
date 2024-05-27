#!/usr/bin/python3
"""This module defines a function to create an Object
from a JSON file."""

import json


def load_from_json_file(filename):
    """
    load_from_json_file - Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

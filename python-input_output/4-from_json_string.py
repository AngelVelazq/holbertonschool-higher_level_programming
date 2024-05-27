#!/usr/bin/python3
""" module defines a function to return a Python data
structure represented by a JSON string."""

import json


def from_json_string(my_str):
    """
    from_json_string - Returns a Python data structure represented by a JSON
    string.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

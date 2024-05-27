#!/usr/bin/python3
"""This module defines a function to return the JSON
representation of an object (string)."""


def to_json_string(my_obj):
    """
    to_json_string - Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON representation of the object.
    """
    if isinstance(my_obj, str):
        return '"' + my_obj.replace('"', '\\"') + '"'
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, bool):
        return "true" if my_obj else "false"
    elif my_obj is None:
        return "null"
    elif isinstance(my_obj, list):
        return "[" + ", ".join(to_json_string(i) for i in my_obj) + "]"
    elif isinstance(my_obj, set):
        return "[" + ", ".join(to_json_string(i) for i in sorted(my_obj)) + "]"
    elif isinstance(my_obj, dict):
        items = (f"{to_json_string(k)}: {to_json_string(v)}"
                 for k, v in my_obj.items())
        return "{" + ", ".join(items) + "}"
    else:
        raise TypeError
    (f"Object of type '{type(my_obj).__name__}' is not JSON serializable")

#!/usr/bin/python3
"""Module defined to write string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number of characters

    Args:
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

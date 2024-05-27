#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty
        string.
        The text to append to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added to the file."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

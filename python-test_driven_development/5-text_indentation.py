#!/usr/bin/python3
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        # Add the character to the result string
        result += char
        # Add two new lines after '.', '?', and ':'
        if char in ['.', '?', ':']:
            result += '\n\n'

    return result

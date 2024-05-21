#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    new_text = ''
    skip_space = False

    for char in text:
        if char in punctuations:
            new_text += char + '\n\n'
            skip_space = True  # Skip space after punctuation
        elif char == ' ' and skip_space:
            skip_space = False  # Skip adding this space
        else:
            new_text += char
            skip_space = False  # Reset skip_space if it's not a space

    lines = new_text.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Print non-empty lines only
            print(stripped_line)

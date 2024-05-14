#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""
    # Iterate over each character in the input string
    for char in my_string:
        # Check if the character is 'c' or 'C'
        if char != 'c' and char != 'C':
            # If not, append it to the result string
            result += char
    # Return the result string
    return result

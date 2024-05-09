#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase using ASCII values
            result += chr(ord(char) - 32)
            # ASCII values of lowercase letters are 32 greater than uppercase
        else:
            result += char

    print("Uppercase string:", result)

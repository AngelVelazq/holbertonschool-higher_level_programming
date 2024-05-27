#!/usr/bin/python3
"""
0-read_file.py - This module defines a function to read and print a text file.
"""


def read_file(filename=""):
    """
    read_file - Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

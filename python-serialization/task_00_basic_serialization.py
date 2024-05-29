#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    :param data: A Python Dictionary with data
    :param filename: The filename of the output JSON file.
    If the output file already exists, it should be replaced."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary.

    :param filename: The filename of the input JSON file
    :return: A Python Dictionary with the deserialized
    JSON data from the file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print("An error occurred while reading from the file or decoding "
              f"JSON: {e}")
        return None

import json


def serialize_and_save_to_file(data, filename):
    """Args:
        data (dict): Python dictionary containing the data to be serialized.
        filename (str): The filename of the output JSON file.
        If the file already exists, it will be replaced.
        Returns: None
        """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from the specified file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data from the file
        """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

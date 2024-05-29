import json


def serialize_and_save_to_file(data, filename):
    """Args:
        data (dict): Python dictionary containing the data to be serialized.
        filename (str): The filename of the output JSON file.
        If the file already exists, it will be replaced.

    Returns:
        None"""
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


# Example usage
if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize the given Python dictionary into XML
    and save it to the specified file.

    Args:
        dictionary (dict): Python dictionary to be serialized.
        filename (str): The filename of the output XML file."""
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from the specified file
    and reconstruct the Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: A Python dictionary reconstructed from the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text

    for key, value in data_dict.items():
        if value.isdigit():
            data_dict[key] = int(value)
        elif '.' in value and all(
            char.isdigit() or char == '.'
            for char in value
        ):
            data_dict[key] = float(value)

    return data_dict


if __name__ == "__main__":
    # Testing the functions
    sample_dict = {
        'name': 'John',
        'age': 28,
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

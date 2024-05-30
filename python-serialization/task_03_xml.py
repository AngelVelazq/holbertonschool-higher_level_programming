#!/usr/bin/python3
""" Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET
"""explore serialization and deserialization using XML"""


def serialize_to_xml(dictionary, filename):
    """Serialize the given Python dictionary into XML
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
    tree = ET.parse(filename) # Parse the XML file
    root = tree.getroot() # Get the root element

    data_dict = {}

    # Navigate through XML elements to reconstruct the dictionary
    for child in root:
        data_dict[child.tag] = child.text # Use data_dict to store the key-value pairs


    return data_dict

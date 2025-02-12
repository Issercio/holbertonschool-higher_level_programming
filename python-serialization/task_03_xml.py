#!/usr/bin/env python3
'''xml
'''


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename to save the XML data.
    """
    try:
        # Create the root element
        root = ET.Element("data")

        # Iterate through the dictionary and add elements
        for key, value in dictionary.items():
            element = ET.SubElement(root, key)
            element.text = str(value)

        # Write the XML to a file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception as e:
        print(f"Serialization error: {e}")


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Parameters:
    filename (str): The XML filename to read from.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Convert XML elements into a dictionary
        return {child.tag: child.text for child in root}

    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Deserialization error: {e}")
        return None

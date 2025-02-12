#!/usr/bin/env python3
'''basic_serialization
'''


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The name of the JSON file to save the data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to a Python dictionary.

    Parameters:
    filename (str): The name of the JSON file to load data from.

    Returns:
    dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)

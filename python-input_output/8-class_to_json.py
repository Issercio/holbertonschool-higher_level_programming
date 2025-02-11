#!/usr/bin/python3


def class_to_json(obj):
    """Returns the dictionary description of the object for JSON serialization."""
    # Create an empty dictionary to hold the object attributes
    obj_dict = {}

    # Loop through the object's __dict__ (which contains the attributes of the instance)
    for attr, value in obj.__dict__.items():
        # Check if the attribute value is a simple data type
        if isinstance(value, (str, int, float, bool, list, dict)):
            obj_dict[attr] = value
    
    return obj_dict

#!/usr/bin/python3
'''class_to_json
'''


def class_to_json(obj):
    """Returns the dictionary description"""
    obj_dict = {}

    for attr, value in obj.__dict__.items():
        # Check if the attribute value is a simple data type
        if isinstance(value, (str, int, float, bool, list, dict)):
            obj_dict[attr] = value

    return obj_dict

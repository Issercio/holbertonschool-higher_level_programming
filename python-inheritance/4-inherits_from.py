#!/usr/bin/python3
"""4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    """
    return isinstance(obj, a_class) and type(obj) != a_class

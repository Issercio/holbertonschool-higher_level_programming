#!/usr/bin/python3
"""Module containing say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'."""
    
    # Check if first_name and last_name are strings
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")

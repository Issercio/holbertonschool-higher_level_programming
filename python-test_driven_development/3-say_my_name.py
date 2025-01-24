#!/usr/bin/python3
"""Module containing say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Function printing "My name is <first name> <last name>"""""

    # Checking if first_name and last_name are not strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Printing the statement
    print("My name is {} {}".format(first_name, last_name))
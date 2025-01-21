#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Replace the value for the existing key, or add the key/value pair if it doesn't exist
    a_dictionary[key] = value
    return a_dictionary

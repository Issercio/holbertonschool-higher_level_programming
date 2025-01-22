#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If a ValueError or TypeError occurs, return False
        return False
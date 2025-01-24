#!/usr/bin/python3
"""Module containing print_square function"""


def print_square(size):
    """Prints a square with the character #."""
    
    # Check if size is an integer
    if type(size) is not int:
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # If size is a float and less than 0, raise a TypeError
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    
    # Print the square
    for _ in range(size):
        print("#" * size)

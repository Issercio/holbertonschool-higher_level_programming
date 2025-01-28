#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.

        Args:
            size (int): The size of the square. Must be an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

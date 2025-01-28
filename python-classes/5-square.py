#!/usr/bin/python3
class Square:
    """Class that defines a square with a private instance attribute `size`."""

    def __init__(self, size=0):
        """
        Initialize the square with a private instance attribute `size`.
        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size  # Using the setter to initialize and validate `size`.

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set and validate the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current square area.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#' to stdout.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

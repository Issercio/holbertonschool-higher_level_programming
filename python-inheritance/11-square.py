#!/usr/bin/python3
"""11-square.py
"""


class BaseGeometry:
    """A class representing BaseGeometry"""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Instantiates a Rectangle object with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class representing a square that inherits from Rectangle."""

    def __init__(self, size):
        """
        Instantiates a Square object with size.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"

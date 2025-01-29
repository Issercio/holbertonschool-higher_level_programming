#!/usr/bin/python3

'''
Module for Class Rectangle
'''


class Rectangle:
    '''Defines a rectangle'''

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialize the rectangle with optional width and height'''
        self.width = width
        self.height = height
        # Increment the number of instances whenever a new Rectangle is created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width with validation'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height with validation'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Returns a string representation of the rectangle using the print_symbol'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        '''Returns a string representation that can recreate the rectangle'''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''Prints a message when the instance is deleted and decrement the number of instances'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area, or rect_1 if both are equal'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        '''Returns a new Rectangle instance where width == height == size'''
        return cls(size, size)

#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''A class representing a square.'''

    def __init__(self, size=0):
        '''Initialize the square with a specified size.'''
        self.__set_size(size)

    def __set_size(self, value):
        '''Private method to set the size with validation.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def get_size(self):
        '''Getter method for size.'''
        return self.__size

    def set_size(self, value):
        '''Setter method for size with validation.'''
        self.__set_size(value)

    size = property(get_size, set_size)

    def area(self):
        '''Calculate and return the area of the square.'''
        return self.__size ** 2

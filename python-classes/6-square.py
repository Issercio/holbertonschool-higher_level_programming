#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''A class representing a square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize the square with a given size and position.'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieve the size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square with validation.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Retrieve the position of the square.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set the position of the square with validation.'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Return the area of the square.'''
        return self.size ** 2

    def my_print(self):
        '''Print the square using the character #.'''
        if self.size == 0:
            print()
            return

        print("\n" * self.position[1], end="")

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
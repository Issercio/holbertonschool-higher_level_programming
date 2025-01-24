#!/usr/bin/python3
"""
This is the divide module.
has a function to divide matrix
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and rounds the result to 2 decimal places."""
    
    # Check if matrix is a list of lists
    if type(matrix) is not list or not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row in the matrix has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number (int or float)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix with elements divided by div, rounded to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]

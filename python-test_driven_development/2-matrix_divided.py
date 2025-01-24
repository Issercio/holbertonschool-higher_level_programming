#!/usr/bin/python3
"""
This is the divide module.
has a function to divide matrix
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor (integer or float).

    Returns:
        A new matrix with each element of the input matrix divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows in the matrix are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division
    return [[round(num / div, 2) for num in row] for row in matrix]

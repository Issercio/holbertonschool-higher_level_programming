#!/usr/bin/python3
'''model_class_pascal
'''


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Every row starts with 1

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)  # Add new row to the triangle

    return triangle

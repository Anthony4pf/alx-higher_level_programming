#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module supplies a function for the division of a matrix
"""


def matrix_divided(matrix, div):
    """Divides a matrix with div and returns a new matrix"""
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix  for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    if not all(row_len == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]

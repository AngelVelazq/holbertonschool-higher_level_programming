#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with all elements divided by div.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats,
                   or if rows are not of the same size,
                   or if div is not an integer/float.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or not all(isinstance(row, list)
        for row in matrix) or not all(isinstance(el, (int, float))
                                      for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]

#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats, or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
        >>> matrix_divided([[1, 2, 3], [4, 5]], 2)
        Traceback (most recent call last):
            ...
        TypeError: Each row of the matrix must have the same size
        >>> matrix_divided([[1, 2, 3], [4, '5', 6]], 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]


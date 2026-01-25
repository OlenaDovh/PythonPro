from typing import List

import numpy


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Множить дві матриці.

    >>> matrix_multiply([[1],[2]], [[3],[4]])
    Traceback (most recent call last):
        ...
    ValueError: Number of columns in the first matrix must match number of rows in the second matrix

    >>> matrix_multiply([[1,2],[3,4]], [[5,6],[7,8]])
    [[19, 22], [43, 50]]

    >>> matrix_multiply([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]])
    [[58, 64], [139, 154]]

    >>> matrix_multiply([[1]], [[2]])
    [[2]]

    >>> matrix_multiply([[1,2]], [[3],[4]])
    [[11]]

    >>> matrix_multiply([[1,2]], [[3,4]])
    Traceback (most recent call last):
        ...
    ValueError: Number of columns in the first matrix must match number of rows in the second matrix

    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix "
                         "must match number of rows in the second matrix")
    return numpy.dot(matrix1, matrix2).tolist()


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Транспонує матрицю.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    >>> transpose_matrix([[1, 2, 3], [3, 4, 5]])
    [[1, 3], [2, 4], [3, 5]]

    >>> transpose_matrix([[1]])
    [[1]]

    >>> transpose_matrix([[2],[3]])
    [[2, 3]]

    >>> transpose_matrix([])
    []

    """
    return numpy.transpose(matrix).tolist()

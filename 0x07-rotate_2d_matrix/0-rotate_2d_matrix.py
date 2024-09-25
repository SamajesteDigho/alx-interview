#!/usr/bin/python3
""" Rotating 2D Matrix module
"""
from typing import Any, List


def check_is_matrix(matrix: Any) -> bool:
    """ Check if a matrix is squared """
    if not isinstance(matrix, list):
        return False
    elif not all(map(lambda x: isinstance(x, list), matrix)):
        return False
    return True


def check_is_squared(matrix: List[List[Any]]) -> bool:
    if not isinstance(matrix, list):
        return False
    if len(matrix) == 1:
        return True
    length = len(matrix[0])
    if not all(map(lambda x: len(x) == length, matrix)):
        return False
    return True


def rotate_2d_matrix(matrix: List[List[Any]]):
    """ 2D Rotation of Matrix """
    size = len(matrix[0])
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

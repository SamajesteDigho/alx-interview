#!/usr/bin/python3
""" Rotating 2D Matrix module
"""
from typing import Any, List


def rotate_2d_matrix(matrix: List[List[Any]]):
    """ 2D Rotation of Matrix """
    size = len(matrix[0])
    for x in range(0, int(size / 2)):
        for y in range(x, size-x-1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[size-1-y][x]
            matrix[size-1-y][x] = matrix[size-1-x][size-1-y]
            matrix[size-1-x][size-1-y] = matrix[y][size-1-x]
            matrix[y][size-1-x] = tmp

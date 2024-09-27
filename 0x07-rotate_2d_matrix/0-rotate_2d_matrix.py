#!/usr/bin/python3
""" Rotating 2D Matrix module
"""
from typing import Any, List


def anti_clock_wise_rotation(matrix: List[List[Any]], size: int):
    """ Anti-clockwise rotation """
    for x in range(0, int(size / 2)):
        for y in range(x, size-x-1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[y][size-1-x]
            matrix[y][size-1-x] = matrix[size-1-x][size-1-y]
            matrix[size-1-x][size-1-y] = matrix[size-1-y][x]
            matrix[size-1-y][x] = tmp


def clock_wise_rotation(matrix: List[List[Any]], size: int):
    """ Clock wise rotation """
    for x in range(0, int(size / 2)):
        for y in range(x, size-x-1):
            tmp = matrix[x][y]
            matrix[x][y] = matrix[size-1-y][x]
            matrix[size-1-y][x] = matrix[size-1-x][size-1-y]
            matrix[size-1-x][size-1-y] = matrix[y][size-1-x]
            matrix[y][size-1-x] = tmp


def rotate_2d_matrix(matrix: List[List[Any]]):
    """ 2D Rotation of Matrix """
    size = len(matrix[0])
    clock_wise_rotation(matrix=matrix, size=size)

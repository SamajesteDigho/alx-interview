#!/usr/bin/python3
"""
    In this module file we define a function used to print the pascal triangle
"""


def get_new_row(prev_row: list, level: int) -> list:
    """ Get the previous row and return the new row """
    if level == 0:
        return [1]
    new = [1]
    size = len(prev_row)
    for x in range(0, size):
        if x <= size - 2:
            new.append(prev_row[x] + prev_row[x + 1])
    new.append(1)
    return new


def pascal_triangle(n) -> list:
    """ Given an integer n, we write down the Pascal Triangle of this one """
    if n <= 0:
        return []
    pascaline = []
    row = []
    for level in range(n):
        row = get_new_row(row, level)
        pascaline.append(row)

    return pascaline

#!/usr/bin/python3
""" Module perimeter of the island
"""


def get_perimeter(grid, row, col):
    """ Get the perimeter of a square """
    if grid[row][col] == 0:
        return 0
    else:
        count = 0
        try:
            if grid[row-1][col] == 0:
                count += 1
        except IndexError:
            count += 1
        try:
            if grid[row+1][col] == 0:
                count += 1
        except IndexError:
            count += 1
        try:
            if grid[row][col-1] == 0:
                count += 1
        except IndexError:
            count += 1
        try:
            if grid[row][col+1] == 0:
                count += 1
        except IndexError:
            count += 1
        return count


def island_perimeter(grid):
    """ Let's get the perimeter of the island """
    if not isinstance(grid, list):
        return 0
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])
    perimeter = 0
    for i in range(n):
        try:
            for j in range(m):
                perimeter += get_perimeter(grid, i, j)
        except Exception:
            pass
    return perimeter

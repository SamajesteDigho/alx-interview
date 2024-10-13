#!/usr/bin/python3
""" Module perimeter of the island
"""


def get_perimeter(grid, size, row, col):
    """ Get the perimeter of a square """
    if grid[row][col] == 0:
        return 0
    else:
        count = 0
        # Check West direction
        if row - 1 < 0:
            count += 1
        elif grid[row-1][col] == 0:
            count += 1
        # Check East direction
        if row + 1 >= size[0]:
            count += 1
        elif grid[row+1][col] == 0:
            count += 1
        # Check North direction
        if col - 1 < 0:
            count += 1
        elif grid[row][col-1] == 0:
            count += 1
        # Check South direction
        if col + 1 >= size[1]:
            count += 1
        elif grid[row][col+1] == 0:
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
    try:
        for i in range(n):
            for j in range(m):
                perimeter += get_perimeter(grid, (n, m), i, j)
    except Exception as e:
        print(e)
        return 0
    return perimeter

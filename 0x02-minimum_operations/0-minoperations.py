#!/usr/bin/env python3
"""
    The module for Minimum Operation Determination
"""
from typing import List, Tuple


def fragment_number(n: int) -> Tuple[int, int]:
    """ Fragment a given number into the 2 closest multiple """
    pair: Tuple = tuple([1, n])
    for i in range(2, n//2 + 1):
        mod: int = n % i
        if mod == 0 and abs(i - n//i) < abs(pair[0] - pair[1]):
            pair = tuple([i, n//i])
    return pair


def get_associate_pairs(n: int) -> List[Tuple[int, int]]:
    """ Get the next child pair """
    branches: List[Tuple[int, int]] = []
    current: Tuple[int, int] = fragment_number(n)
    while current[0] != 1 and current[1] != 1:
        branches.append(current)
        current = fragment_number(current[0])
    branches.append(current)
    return branches


def gathering_operations(graph: List[Tuple[int, int]]) -> int:
    """ Gathering and calulating the number of operations """
    sum: int = 0
    for _, y in graph:
        sum += y
    return sum


def minOperations(n: int) -> int:
    """ Here the principal function for getting the number of operations """
    return gathering_operations(get_associate_pairs(n))

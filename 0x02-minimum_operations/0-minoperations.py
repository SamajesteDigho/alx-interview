#!/usr/bin/python3
"""
    The module for Minimum Operation Determination
"""
from typing import Tuple


def fragment_number(n: int) -> Tuple[int, int]:
    """ Fragment a given number into the 2 closest multiple """
    pair: Tuple = tuple([1, n])
    for i in range(2, n//2 + 1):
        mod: int = n % i
        if mod == 0 and abs(i - n//i) < abs(pair[0] - pair[1]):
            pair = tuple([i, n//i])
    return pair


def process_node(node: Tuple[int, int]) -> int:
    """ Process a node [x, y] and return the number of operations """
    if node[0] == 1:
        return node[1]
    if node[1] == 1:
        return node[0]
    left: Tuple[int, int] = fragment_number(n=node[0])
    right: Tuple[int, int] = fragment_number(n=node[1])
    return process_node(node=left) + process_node(node=right)


def minOperations(n: int) -> int:
    """ Here the principal function for getting the number of operations """
    initial: Tuple[int, int] = fragment_number(n=n)
    return process_node(node=initial)

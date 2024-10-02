#!/usr/bin/python3
""" Here the module of the project
"""


def makeChange(coins, total):
    """ Get the lowest number of coins """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    number = 0
    rest = total
    for coin in coins:
        if rest // coin > 0:
            plus = int(rest / coin)
            number += plus
            rest -= plus * coin
    if rest != 0:
        return -1
    return number

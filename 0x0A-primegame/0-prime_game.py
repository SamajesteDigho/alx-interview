#!/usr/bin/python3
""" Here module foor getting the module
"""


def playOneRound(nb):
    """ Play one round and return winner """
    number_set = [x for x in range(2, nb + 1)]
    turn = 1
    MARIA = []
    BEN = []
    while len(number_set) > 0:
        selected = number_set[0]
        TEMP = []
        for x in number_set:
            if x % selected == 0:
                TEMP.append(x)
                number_set.remove(x)
        if turn == 1:
            MARIA.extend(TEMP)
            TEMP = []
            turn = 2
        else:
            BEN.extend(TEMP)
            TEMP = []
            turn = 1
    if turn == 1:
        return 2
    else:
        return 1


def isWinner(x, nums):
    """ Here the winner function """
    counts = {'Maria': 0, 'Ben': 0}
    round = 0
    for nb in nums:
        try:
            if round >= x:
                break
            else:
                round += 1
            winner = playOneRound(nb)
            if winner == 1:
                counts['Maria'] += 1
            else:
                counts['Ben'] += 1
        except Exception:
            pass
    if counts['Maria'] > counts['Ben']:
        return 'Maria'
    else:
        return 'Ben'

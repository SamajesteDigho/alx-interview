#!/usr/bin/python3
"""
    This code module permits us to tacle the problem of lock blocks
"""


def markBlockAsVisited(index, stv, arv):
    """ Node marker """
    if stv.__contains__(index):
        stv.remove(index)
    arv.add(index)
    return stv, arv


def visitNodes(boxes, index, stv, arv):
    """ Nodes Visiting contest """
    stv, arv = markBlockAsVisited(index, stv=stv, arv=arv)
    if index >= len(boxes):
        return stv, arv
    if len(boxes[index]) == 0:
        return stv, arv

    for x in boxes[index]:
        if not arv.__contains__(x):
            stv, arv = visitNodes(boxes, x, stv, arv)
    return stv, arv


def canUnlockAll(boxes) -> bool:
    """
        This function determines if all blocks can be opened
        and return True or False
    """
    if not isinstance(boxes, list):
        return False
    if len(boxes) == 0:
        return True
    remain = set([x for x in range(len(boxes))])
    visited = set()
    remain, visited = visitNodes(boxes, 0, stv=remain, arv=visited)

    if len(remain) == 0:
        return True
    else:
        return False

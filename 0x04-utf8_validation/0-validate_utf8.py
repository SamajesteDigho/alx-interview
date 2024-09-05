#!/usr/bin/python3
"""
    UTF8 Bit vlidation exercise
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Validate data as utf8 character """
    for x in data:
        if x < 0 or x >= 256:
            return False
    return True

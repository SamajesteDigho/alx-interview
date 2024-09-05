#!/usr/bin/python3
"""
    UTF8 Bit vlidation exercise
"""
from typing import List, Tuple, Union


def convert_nb_to_binary(nb: int) -> str:
    """ Convert nb to binary """
    return "{0:08b}".format(nb)


def check_step_1(val: str) -> Union[int, None]:
    """ Check UTF8 first byte conformity and give the number
        of bytes on which the data is encoded
    """
    if len(val) < 1 or len(val) > 8:
        return None
    if val[0] == '0':
        return 1
    elif val[0:3] == '110':
        return 2
    elif val[0:4] == '1110':
        return 3
    elif val[0:5] == '11110':
        return 4
    return None


def process_current_byte_validate_next(data: List[str],
                                       byte_idx: int,
                                       nb_byte: Union[int, None]
                                       ) -> Tuple[bool, int]:
    """ Process the current byte structure and validate the next bytes """
    count = 0
    if nb_byte is None:
        return (False, count)
    elif nb_byte < 0 or nb_byte > 4:
        return (False, count)
    elif nb_byte == 1 and data[byte_idx][0] == '0':
        return (True, count)
    elif nb_byte != 1 and data[byte_idx][nb_byte] != '0':
        return (False, count)

    for x in range(byte_idx+1, byte_idx+nb_byte):
        try:
            count += 1
            if data[x][0:2] != '10':
                return (False, count)
        except Exception:
            return (False, count)
    return (True, count)


def validUTF8(data: List[int]) -> bool:
    """ Validate data as utf8 character """
    binaries = [convert_nb_to_binary(x) for x in data]
    for cur in range(len(data)):
        nbb = check_step_1(binaries[cur])
        good, added = process_current_byte_validate_next(
            data=binaries, byte_idx=cur, nb_byte=nbb)
        if not good:
            return False
        cur += added
    return True

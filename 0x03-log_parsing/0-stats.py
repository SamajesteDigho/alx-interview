#!/usr/bin/python3
"""
    Here the module description
"""
import re
import signal
import sys
from typing import Any


data = {}
size = 0
count = 0
code_list = ['200', '301', '400', '401', '403', '404', '405', '500']


def display_info():
    """  Display information as formatted """
    global data, size
    print("File size: {}".format(size))
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, data[key]))


def line_match_regex(line: str) -> bool:
    """ Check if the line matches the regex """
    ip_reg = r'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}'\
        '([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    dt_reg = r'\[[0-9]{4}-(0[1-9]|1[0-2])-([0-2][1-9]|30|31) '\
        r'([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\.[0-9]{6}\]'
    sc_reg = r'(200|301|400|401|403|404|405|500|Hello){1}'
    fs_reg = r'([1-9][0-9]*){1}'
    fixed = '"GET /projects/260 HTTP/1.1"'
    regex = f'{ip_reg} - {dt_reg} {fixed} {sc_reg} {fs_reg}'
    match = re.fullmatch(pattern=regex, string=line)
    if match is None:
        regex = r".* {} {}".format(sc_reg, fs_reg)
        match = re.fullmatch(pattern=regex, string=line)
        if match is None:
            return False
        return True
    return True


def process_input(input: str):
    """ Process input and classify it """
    global data, size, code_list
    parts = input.split(sep=' ')
    status = parts[-2]
    addsize = int(parts[-1])
    if status in code_list:
        data[status] = data.get(status, 0) + 1
    size += addsize


def interruption_handle(signum: Any, frame: Any):
    """ Interrupt the process """
    display_info()
    sys.exit(0)


def main():
    """ Main heart function """
    global data, size, count
    for line in sys.stdin:
        if line_match_regex(line.strip()):
            process_input(input=line)
            count += 1
        if count == 10:
            display_info()
            count = 0
    display_info()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, interruption_handle)
    main()

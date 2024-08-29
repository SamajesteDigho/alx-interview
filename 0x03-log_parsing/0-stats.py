#!/usr/bin/python3
"""
    Here the module description
"""
import signal
import sys


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
    if len(line) == 0:
        False
    return True


def process_input(input: str) -> bool:
    """ Process input and classify it """
    global data, size, code_list
    parts = input.split(sep=' ')
    status = parts[-2]
    addsize = int(parts[-1])
    if status in code_list:
        data[status] = data.get(status, 0) + 1
        size += addsize
        return True
    return False


def interruption_handle(signum, frame):
    """ Interrupt the process """
    display_info()
    sys.exit(0)


def main():
    """ Main heart function """
    global data, size, count
    for line in sys.stdin:
        if line_match_regex(line):
            process_input(input=line)
            count += 1
        if count == 10:
            display_info()
            count = 0


if __name__ == "__main__":
    signal.signal(signal.SIGINT, interruption_handle)
    main()

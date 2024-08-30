#!/usr/bin/python3

import random
import sys
from time import sleep

with open("data.txt") as file:
    line = file.read()
    sleep(random.random())
    sys.stdout.write(line)
    sys.stdout.flush()

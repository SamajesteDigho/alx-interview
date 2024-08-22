#!/usr/bin/python3
"""
Main file for testing
"""

import time


minOperations = __import__('0-minoperations').minOperations
start = time.perf_counter()
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
end = time.perf_counter()
print("For a total time of : {}".format(end - start))

start = time.perf_counter()
n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
end = time.perf_counter()
print("For a total time of : {}".format(end - start))

start = time.perf_counter()
n = 2000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
end = time.perf_counter()
print("For a total time of : {}".format(end - start))

#!/usr/bin/python3
"""
Main file for testing
"""
import time


minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
start = time.perf_counter()
n = 2147483640
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
end = time.perf_counter()
print("Time is : {}".format(end -start))

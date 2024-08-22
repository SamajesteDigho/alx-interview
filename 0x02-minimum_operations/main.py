#!/usr/bin/python3
"""
Main file for testing
"""
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 16
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 10000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


n = 20000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 30000
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

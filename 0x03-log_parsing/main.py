#!/usr/bin/python3

test_regex = __import__("0-stats").line_match_regex

# path = '16.237.46.195 - [2024-08-30 08:23:57.876366] "GET /projects/260 HTTP/1.1" 405 120'
path = '16.237.46.195 - [2024-08-30 08:23:57.876366] "GET /projects/260 HTTP/1.1" 405 120'
print(test_regex(path))
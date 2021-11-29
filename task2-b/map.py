#!/usr/bin/python

import sys

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = value.strip().split(',')
    if float(value[-1]) <= 15: print "15\t1"

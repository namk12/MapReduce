#!/usr/bin/python

import sys

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = value.strip().split(',')
    print "%s\t1" % (value[3])

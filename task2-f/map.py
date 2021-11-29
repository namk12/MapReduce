#!/usr/bin/python

import sys

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    key = key.strip().split(',')
    print "%s\t%s" % (key[1], key[0])


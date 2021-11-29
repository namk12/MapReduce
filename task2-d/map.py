#!/usr/bin/python

import sys

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    key = key.strip().split(',')[-1].split(' ', 1)[0]
    value = value.strip().split(',')
    revenue = float(value[11]) + float(value[12]) + float(value[14])
    tip = float(value[14])
    print "%s\t%.2f,%.2f" % (key,revenue,tip)
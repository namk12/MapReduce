#!/usr/bin/python

import sys

for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = value.strip().split(',')
    if 0 <= float(value[11]) and float(value[11]) <= 20: print "0,20\t1"
    elif 20.01 <= float(value[11]) and float(value[11]) <= 40: print "20.01,40\t1"
    elif 40.01 <= float(value[11]) and float(value[11]) <= 60: print "40.01,60\t1"
    elif 60.01 <= float(value[11]) and float(value[11]) <= 80: print "60.01,80\t1"
    elif 80.01 <= float(value[11]): print "80.01,infinite\t1"

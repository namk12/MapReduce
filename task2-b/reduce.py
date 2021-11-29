#!/usr/bin/python

import sys

current_bin = None
current_sum = 0
for line in sys.stdin:
    bin, count = line.strip().split("\t", 1)
    try:
        count = int(count)
    except ValueError:
        continue    
    if bin == current_bin:
        current_sum += count
    else:
        current_bin = bin
        current_sum = count
print "%d" %(current_sum)
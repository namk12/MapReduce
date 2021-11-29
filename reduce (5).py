#!/usr/bin/python

import sys

current_taxi = None
current_sum = 0
days = 0
for line in sys.stdin:
    taxi, count = line.strip().split("\t", 1)
    try:
        count = float(count)
    except ValueError:
        continue    
    if taxi == current_taxi:
        current_sum += count
        days += 1
    else:
	days = 1
        if current_taxi:
            print "%s\t%d,%0.2f" % (current_taxi, current_sum, current_sum/days)
        current_taxi = taxi
        current_sum = count

if current_taxi:
    print "%s\t%d,%0.2f" % (current_taxi, current_sum, current_sum/days)

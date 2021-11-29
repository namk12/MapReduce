#!/usr/bin/python

import sys

current_day = None
current_revenue_sum, current_tip_sum = 0, 0
for line in sys.stdin:
    day, value = line.strip().split("\t")
    revenue, tip = value.strip().split(",")
    try:
        revenue = float(revenue)
        tip = float(tip)
    except ValueError:
        continue    
    if day == current_day:
        current_revenue_sum += revenue
        current_tip_sum += tip
    else:
        if current_day:
            print "%s\t%.2f,%.2f" % (current_day,current_revenue_sum,current_tip_sum)
        current_day = day
        current_revenue_sum = revenue
        current_tip_sum = tip
if current_day:
    print "%s\t%.2f,%.2f" % (current_day,current_revenue_sum,current_tip_sum)
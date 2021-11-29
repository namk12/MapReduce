#!/usr/bin/python

import sys

taxi_pool = dict()
for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    taxi = key.strip().split(',')[0]
    day = key.strip().split(',')[3].split(' ', 1)[0]
    taxi_pool[(taxi, day)] = taxi_pool.get((taxi, day), 0) + 1

for (taxi, day) in taxi_pool:
    print "%s\t%d" % (taxi, taxi_pool[(taxi, day)])
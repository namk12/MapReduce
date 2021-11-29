#!/usr/bin/env python

from operator import itemgetter
import sys
from datetime import datetime as dt
from csv import reader

curr_trips = []
curr_fares = []
curr_key = None
for line in sys.stdin:
    key, value = line.strip().split('\t', 1)
    value = value.strip().split(',')
    if curr_key == None:
        curr_key = key
    # buffer the value
    if curr_key == key:
        if value[0]=='t':
	    value.pop(0)
            curr_trips.append(value)
        elif value[0]=='f':
	    value.pop(0)
            curr_fares.append(value)

    # We've read all the lines which have the same key, do many-to-many join and update to buffer new lines
    else:
        if curr_key != None:
            # TODO: many-to-many join
	    for i in curr_trips:
		for j in curr_fares:
		    print "%s\t%s,%s" %(curr_key, ','.join(i), ','.join(j))
        # update key
        curr_key = key
        # clean buffer
        curr_trips = []
        curr_fares = []
        # buffer the value
        if value[0]=='t':
	    value.pop(0)
            curr_trips.append(value)
        elif value[0]=='f':
	    value.pop(0)
            curr_fares.append(value)

# do not forget to output the last part if needed!
if curr_key == key:
    # TODO: many-to-many join
    for i in curr_trips:
	for j in curr_fares:
	    print "%s\t%s,%s" %(curr_key, ','.join(i), ','.join(j))

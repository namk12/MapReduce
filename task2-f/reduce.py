#!/usr/bin/python

import sys

m = {}
for line in sys.stdin:
    lic, med = line.strip().split("\t", 1)
    if m.get(lic,None)!=None:
        if med in m[lic]:
            continue
        else:
            m[lic].append(med)
    else:
        m[lic] = [med]
        
for key,value in m.items():
    print "%s\t%d" %(key,len(value))

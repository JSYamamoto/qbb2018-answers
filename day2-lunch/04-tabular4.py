#!/usr/bin/env python3

#lunch3
import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

count_t=0
perf=0
oneloc=0
for i, line in enumerate( f ):
    if "NH:i:1" in line:
        oneloc+=1
print("reads that map to exactly one location = " +str(oneloc))
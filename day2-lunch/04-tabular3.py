#!/usr/bin/env python3

#lunch2
import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

count_t=0
perf=0
oneloc=0
for i, line in enumerate( f ):
    if "NM:i:0" in line:
        perf+=1
print("aligns that match perfectly = " +str(perf))
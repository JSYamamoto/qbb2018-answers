#!/usr/bin/env python3

#lunch1
import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

count_t=0
for i, line in enumerate( f ):
   #one way to skip header
    if  line.startswith("@SQ"):
        continue
    if line.startswith("SRR072893"):
        count_t+=1
print("total number of alignments = ", count_t)
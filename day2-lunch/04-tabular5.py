#!/usr/bin/env python3

#lunch4
import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

count_t=0
for i, line in enumerate( f ):
    cut = line.strip().split("\t")
    if count_t >9:
        break
print("chromosome alignment = " +str(cut[2]))  
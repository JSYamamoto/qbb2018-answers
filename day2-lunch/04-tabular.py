#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

count_t=0
perf=0
oneloc=0
for i, line in enumerate( f ):
   #one way to skip header
    if  line.startswith("@SQ"):
        continue
    if line.startswith("SRR072893"):
        count_t+=1
    if "NM:i:0" in line:
        perf+=1 
    if "NH:i:1" in line:
        oneloc+=1
    cut = line.strip().split("\t")
    if count_t >9:
        break
        
print("total number of alignments = ", count_t)
print("aligns that match perfectly = " +str(perf))
print("reads that map to exactly one location = " +str(oneloc))
print("chromosome alignment = " +str(cut[2]))      


#!/usr/bin/env python3

"""
Usage: ./Week8.py /Users/cmdb/qbb2018-answers/Week8/ER4_peaks.narrowPeak.bed
"""

import sys
import matplotlib.pyplot as plt

#Input#
Bed = open(sys.argv[1])

#Def#
Percentage = []

#Grab value & calculate#
for count, line in enumerate(Bed):
    "Skip the header"
    if line.startswith("#"):
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        #print(fields)
        sm = float(fields[3])
        em = float(fields[4])
        sp = float(fields[10])
        ep = float(fields[11])
    #print(sm,em,sp,ep)
        percentage = abs((sm-sp)/(ep-sp))
        #print(percentage)
        Percentage.append(percentage)


#Plot#
fig, ax = plt.subplots() 
fig.set_size_inches(12, 9)
plt.hist(Percentage, bins=60, color="red")
ax.set_xlabel("Relative position in the sequences")
ax.set_ylabel("How often the motifs are detected")
fig.suptitle("Top 100 motifs - Week 8 - Density plot")
fig.savefig("Motifs.png")
plt.tight_layout()
plt.close(fig)
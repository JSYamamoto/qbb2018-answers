#!/usr/bin/env python3

# Run with: 
# ./week2_dotplots.py ./sorted_SRVelvet_lastz.out 
# ./week2_dotplots.py ./sorted_BCVelvet_lastz.out 
# ./week2_dotplots.py ./sorted_SRSpades_lastz.out 
# ./week2_dotplots.py ./sorted_BCSpades_lastz.out 
# ./week2_dotplots.py ./sorted_LRSpades_lastz.out

"""
Usage: dotplot.py ./sorted_SRVelvet_lastz.out
"""

import sys
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (8, 6))

lastXEnd = 0
contigDict = {}
referenceDict = {}
filename = open(sys.argv[1])

for i, line in enumerate(filename):
    fields = line.rstrip("\r\n").split("\t")
    if fields[-3] in contigDict:
        contigDict[(fields[-3])].append((int(fields[-2]), int(fields[-1])))
        referenceDict[(fields[-3])].append([int(fields[1]), int(fields[2]), fields[0]])
    else:
        contigDict[(fields[-3])] = [(int(fields[-2]), int(fields[-1]))]
        referenceDict[(fields[-3])] = [(int(fields[1]), int(fields[2]), fields[0])]
for key in contigDict:
    x = []
    y = []
    for valueC in contigDict[key]:
        x1, x2 = valueC
        x1 += lastXEnd
        x2 += lastXEnd
        x.append(x1)
        x.append(x2)
    for valueR in referenceDict[key]:
        y1, y2, strand = valueR
        if strand == "+":
            y.append(y1)
            y.append(y2)
        else:
            y.append(y2)
            y.append(y1)
    for i in range(0, len(x), 2):   
        plt.plot(x[i:i+2], y[i:i+2])  
     
fig.suptitle("Contigs Aligned to Reference",fontsize = 14)
ax.set_xlabel("Contigs", fontsize = 12)
ax.set_ylabel("Position in Reference", fontsize = 12)   
  
#fig.savefig("week2_SRVelvet_dotplot.png")
#fig.savefig("week2_BCVelvet_dotplot.png")
#fig.savefig("week2_SRSpades_dotplot.png")
#fig.savefig("week2_BCSpades_dotplot.png")
fig.savefig("week2_LRSpades_dotplot.png")

plt.close(fig)
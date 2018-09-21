#!/usr/bin/env python3

"""
Usage: to count the number of contigs, min, max, average length, and N50.
<contigs.py> <
"""

import sys
import fasta
import numpy as np


fa_file = fasta.FASTAReader(open(sys.argv[1]))

length_of_contigs=[]

for frag_id,frag in fa_file:
    length=len(frag)
    length_of_contigs.append(length)
    
    
genome_length = sum(length_of_contigs)
count_frag = len(length_of_contigs)
minimum = min(length_of_contigs) 
maximum= max(length_of_contigs)
mean = np.mean(length_of_contigs)

print("Fragment count is = " +str(count_frag), "Min value is = " +str(minimum), "Max value is = " +str(maximum), "Average value is = " +str(mean))

n50_list = sorted(length_of_contigs)

cumulative = 0
for contig in n50_list:
    cumulative +=contig
    if cumulative > (genome_length/2):
        print(contig)
        break



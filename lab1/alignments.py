#!/usr/bin/env python3

"""
./alignments.py> <tabseq.fa> <aminoacids.fa>
"""

import fasta
import sys
import itertools
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os
from statsmodels.stats import weightstats as stest



dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))
n_seq = []
all_aa = []


for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    new_dna = []
    aa_list = []
    j = 0
    for i in range(len(aa)):
        a = aa[i]
        n = dna[j: j + 3]
        #nuc = dna[i*3: (i+1)*3]
        if a == '-':
            n = "---"
            aa_list.append(a)
            new_dna.append(n)
            
        else:
            j +=3
            aa_list.append(a)
            new_dna.append(n)
            
    n_seq.append(new_dna)
    all_aa.append(aa_list)
    
#print(n_seq)
aa_q = all_aa[0]
dna_q = n_seq[0]

#to find synonymous and nonsynonymous changes
dN = [0] * len(aa_q)
dS = [0] * len(dna_q)

for i in range(1, len(all_aa[1:])):
    new_alignment = all_aa[i]
    for j in range(len(new_alignment)):
        if new_alignment[j] != aa_q[j]:
            dN[j] += 1
        else:
            dS[j] +=1
            
#print(dN, dS)
ztest_data = stest.ztest(dN, dS)

dS_dN_ratio = []
for i in range(len(dS)):
    dS_dN = dN[i] / (dS[i] + 1)
    dS_dN_ratio.append(dS_dN)
    
#print(dS_dN_ratio)
 
x = range(0, len(dS_dN_ratio))
y = dS_dN_ratio

fig, ax = plt.subplots()
plt.scatter(x, y, alpha = 0.5, s=3, color = "cyan")
ax.set_title("Synonymous Vs Non Synonymous nucleotide changes at base positions")
ax.set_xlabel("Base position")
ax.set_ylabel("dN/dS")
plt.tight_layout()
fig.savefig("week1_plot")
plt.close(fig)        
        
#!/usr/bin/env python3

"""
Usage: ./gene-name.py <gene_name> <samples.csv> <ctab_dir>

Create a plot for mean values for a gene specified on command line
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


def mean_transcripts(sample, sex, gene):
    df = pd.read_csv(sample)
    soi = df.loc[:, "sex"] == sex
    df = df.loc[soi,:]
    labels = []
    mean_fpkms = []   
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab", )
        ctab_df = pd.read_table(filename, index_col= "t_name")
        roi = ctab_df.loc[:, "gene_name"] == gene
        fpkms = ctab_df.loc[roi, "FPKM"]
        #fpkms.append(ctab_df.loc[roi,"FPKM"])
        mean_fpkms.append(np.mean(fpkms))
        labels.append(stage)
    return mean_fpkms, labels
    
mean_f, labels = mean_transcripts(sys.argv[2],"female", sys.argv[1])
mean_m, labels = mean_transcripts(sys.argv[2], "male", sys.argv[1])

fig,ax = plt.subplots()

ax.plot(mean_m, "b", label= "male",)
ax.plot(mean_f, "r", label= "female",)
fig.suptitle(sys.argv[1])
ax.set_xticklabels(labels, rotation=90)
#fig.suptitle("Abundance of FBtr0331261 in males")
#ax.plot(mean_f, label="Female")
#ax.plot(mean_m, label= "Male")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mean FPKM Abundance")
plt.tight_layout()
box=ax.get_position()
#plt.legend(bbox_to_anchor=(1.07, 0.5), loc=2, borderaxespad=0)
plt.legend()

fig.savefig("gene_name.png", bbox_inches='tight')
plt.close(fig)

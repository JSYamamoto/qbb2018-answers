#!/usr/bin/env python3

"""
Usage: ./day4-homework2.py <t_name> <samples.tsv> <ctab_dir>

Create a plot for abundance of a given transcript ( FBtr0331261) for males
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


#df = pd.read_csv(sys.argv[1])
#soi = df.loc[:, "sex"]
#df = df.loc[soi,:]


def t_course(sex):
    df = pd.read_csv(sys.argv[2])
    soi = df.loc[:, "sex"] == sex
    df = df.loc[soi,:]

    fpkms = []
    stages = []    
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join( sys.argv[3], sample, "t_data.ctab", )
        ctab_df = pd.read_table(filename, index_col="t_name")
    
        roi = ctab_df.loc[:, "gene_name"] == sys.argv[1]
        fpkms.append(ctab_df.loc[sys.argv[1], "FPKM"])
        stages.append(stage)
    return fpkms, stages

fpkms_m, stages = t_course('male')
fpkms_f, stages = t_course('female')

fig,ax = plt.subplots()

ax.plot(fpkms_m, "b", label= "male",)
ax.plot(fpkms_f, "r", label= "female",)
fig.suptitle("FPKM Abundance for males and females")
ax.set_xticklabels(stages, rotation=90)
#fig.suptitle("Abundance of FBtr0331261 in males")
ax.plot(fpkms_m)
ax.plot(fpkms_f)
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("FPKM Abundance")
plt.tight_layout()
box=ax.get_position()
plt.legend(bbox_to_anchor=(1.07, 0.5), loc=2, borderaxespad=0)

fig.savefig("Abundance.png", bbox_inches='tight')
plt.close(fig)




#l = ax.legend(loc="upper right")

#to make legend outside of plot area
# x = np.arange(10)
# fig = plt.figure()
# ax = plt.subplot(111)
# for i in xrange(5):
#     ax.plot(x, i * x, label='$y = %ix$'%i)
#
# # Put a legend to the right of the current axis
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#
# plt.show()

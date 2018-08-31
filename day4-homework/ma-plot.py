#!/usr/bin/env python3

"""
Usage: ./ma-plot.py <sample_file> <sample2_file>


"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")

fpkm1 = df1.loc[:,"FPKM"]
fpkm2 = df2.loc[:,"FPKM"]

fpkm1_log = np.log(fpkm1 +1)
fpkm2_log = np.log(fpkm2 +1)

ratio = np.log2(fpkm1 + 1) - np.log2(fpkm2 + 1)
average = 0.5 * (np.log2(fpkm1 + 1) + np.log2(fpkm2 + 1))

fig, ax = plt.subplots()
ax.scatter(average, ratio, alpha=0.5)

fig.suptitle("FPKM Ma plot")
ax.set_xlabel("average")
ax.set_ylabel("ratio")

fig.savefig("ma-plot.png")
plt.close(fig)




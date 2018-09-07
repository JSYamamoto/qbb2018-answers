#!/usr/bin/env python3

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv (sys.argv[1], sep="\t", index_col = "t_name")
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col = "t_name")

fpkm1 = df1.loc[:,"FPKM"]
fpkm2 = df2.loc[:,"FPKM"]

#fig, ax = plt.subplots()
#fig.suptitle("FPKMs Count of -893 & -915")

fit = np.polyfit(fpkm1, fpkm2, 1)
p = np.poly1d(fit)
xplin = np.linspace(0, fpkm1.max())

fig, ax = plt.subplots()
ax.scatter(fpkm1, fpkm2, alpha=0.1)
plt.plot(xplin, p(xplin), '-', color='m')
#ax.set_xlabel("FPKM1")
#ax.set_ylabel("FPKM2")
plt.yscale("log")
plt.xscale("log")
#ax.set_xscale("log")
#ax.set_yscale("log")
plt.axis([.001, 10000, .001, 10000])
axes = plt.gca
ax.set_title("FPKM1 vs FPKM2")
plt.ylabel("FPKM2")
plt.xlabel("FPKM1")
plt.savefig("FPKM_scatter.png")
plt.close()

#coeff = np.polyfit(fpkm1, fpkm2, 1)
#polynomial = np.poly1d(coeff)
#x = np.linspace(0,10)

#x = np.linspace(0, False, 50)
#y = np.poly1d(0, False, 50)

#ax.set_xlim(0, 20)s
#ax.set_ylim(0, 20)

#plt.plot(x, polynomial(x), 'k')
#plt.text(7,5,str(polynomial))
#ax.scatter (fpkm1, fpkm2)
#fig.savefig("scatter.png")
#plt.close(fig)
#np.polyfit(x,y,deg)
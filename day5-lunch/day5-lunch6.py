#!/usr/bin/env python3
"""
Usage: <./day5-lunch4.py> <tab_file1> <tab_file2> <tab_file3> <tab_file4> <tab_file5>

Plotting residuals with log scale
"""


import sys
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import os


name1 = sys.argv[1].split(os.sep)[-1].split('.')[0] #split on periods because the names had "." in them
m_01 = pd.read_csv (sys.argv[1], sep="\t").iloc[:,4]

name2 = sys.argv[2].split(os.sep)[-1].split('.')[0]
m_02 = pd.read_csv (sys.argv[2], sep="\t").iloc[:,4]

name3 = sys.argv[3].split(os.sep)[-1].split('.')[0]
m_03 = pd.read_csv (sys.argv[3], sep="\t").iloc[:,4]

name4 = sys.argv[4].split(os.sep)[-1].split('.')[0]
m_04 = pd.read_csv (sys.argv[4], sep="\t").iloc[:,4]

name5 = sys.argv[5].split(os.sep)[-1].split('.')[0]
m_05 = pd.read_csv (sys.argv[5], sep="\t").iloc[:,4]

name6 = sys.argv[6].split(os.sep)[-2]
fpkms = pd.read_csv (sys.argv[6], sep="\t").iloc[:,-1]

means0 = {name1 : m_01, name2 : m_02, name3 : m_03, name4 : m_04, name5 : m_05, name6 : fpkms}

means0_df = pd.DataFrame(means0)
means0_df = means0_df.dropna()
#print(means0_df)
y = means0_df.loc[:, name6]
x = means0_df.loc[:,[name1, name2, name3, name4, name5]]
mod = smf.ols(formula = "SRR072893 ~ {} + {} + {} + {} + {}".format(name1, name2, name3, name4, name5,), data=means0_df)
res = mod.fit()
res2= res.resid
#print(res2)
x_axis = res2
y_axis = y


fig, ax = plt.subplots()
ax.hist(res2, bins=5000)
plt.yscale("log")
ax.set_title("Histogram-Residual data")
ax.set_xlabel("resuduals")
ax.set_ylabel("number")
ax.set_xlim(left=-100, right=100)


fig.savefig("residuals_log")
plt.close()

#!/usr/bin/env python3
"""
Usage: <./day5-lunch4.py> <tab_file1> <tab_file2> <tab_file3> <tab_file4> <tab_file5>

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
#print(means0_df)

# mod = smf.ols(formula = "SRR072893 ~ H3K27me3.tab + H3K4me1.tab + H3K4me3.tab + H3K9ac.tab + H3K27ac.tab", data=means0_df)
mod = smf.ols(formula = "SRR072893 ~ {} + {} + {} + {} + {}".format(name1, name2, name3, name4, name5,), data=means0_df)
res = mod.fit()
print(res.summary())
#
# X= df[""]
# y = target[""]
#
# model = sm.OLS(y,X).fit()
# predictions = model.predict(X)
# model.summary()
#!/usr/bin/env python3

"""
Usage: ./day4-lunch.py <treshold> <ctab_file> <ctab_file2>...

Create csv file with FPKMs for two or more samples
- assumes ctab_file in directory with same name 
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

#add different files to dictionary
dict = {}

for i in range(2,len(sys.argv)):
    name1 = sys.argv[i].split(os.sep)[-2]
    fpkm1 = pd.read_csv (sys.argv[i], sep="\t", index_col = "t_name").loc[:,"FPKM"]
    dict[name1]= fpkm1

fpkm_df = pd.DataFrame(dict)
#print(fpkm_df)

fpkm_df.sum = fpkm_df.sum(axis=1)
#print(fpkm_sum)


roi_fpkm = fpkm_df.sum > float(sys.argv[1])
print(roi_fpkm)
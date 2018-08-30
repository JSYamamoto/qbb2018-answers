#!/usr/bin/env python3

"""
Usage: ./day4-homework.py <samples.tsv> <ctab_file> <sex>

Create a list of a given transcript (FBts0331261) for females and males
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])

compiled = {}
#stages = []
for index, sample, sex, stage in df.itertuples():
    filename = os.path.join( sys.argv[2], sample, "t_data.ctab", )
    ctab_df = pd.read_table(filename, index_col="t_name")
    
    
    compiled[sex + "_" + stage] = ctab_df.loc[:, "FPKM"]
dfcompiled = pd.DataFrame(compiled)
print(dfcompiled)
   
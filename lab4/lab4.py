#!/usr/bin/env python3

""""
pca plot <plink.eigenvec>
"""

import sys 
import matplotlib.pyplot as plt
import numpy as np

f1 = open(sys.argv[1])

p1_value = []
p2_value = []

for line in f1:
    fields= line.rstrip("\r\n").split()
    p1_val = fields[2]
    p1_value.append(float(p1_val))
    p2_val = fields[3]   
    p2_value.append(float(p2_val))
    
fig, ax = plt.subplots()
plt.scatter(p1_value,p2_value)
fig.suptitle("PCA")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
fig.savefig("pca.png")
plt.close(fig)


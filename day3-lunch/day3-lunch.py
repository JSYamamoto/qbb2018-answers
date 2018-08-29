#!/usr/bin/env python3

import sys

f = open(sys.argv[1])

count=0

for i, line in enumerate(f):
    if line.startswith ("#"):
        continue
    fields=line.rstrip("\r\n").split()
    if "gene" == fields[2]:
        fields1=fields[2].rstrip("\r\n").split()
        if "gene_biotype" == fields[16]:
            if '"protein_coding";' == fields[17]:
                count += 1
        
print(count)
#!/usr/bin/env python3

import sys

dict={}
f = open(sys.argv[1])


for i, line in enumerate(f):
    if line.startswith ("#"):
        continue
    fields=line.rstrip("\r\n").split()
    if "gene" == fields[2]:
        fields1=fields[2].rstrip("\r\n").split()
        index = fields.index('gene_biotype') + 1
        if fields[index] not in dict.keys():
            dict[fields[index]] = 1
        else:
            dict[fields[index]] += 1        
        # if "gene_biotype" == fields[16]:
        #     if '"protein_coding";' == fields[17]:
        #         count += 1
print(dict)
                
#!/usr/bin/env python3

"""
Examples:
    Run and include no match lines
    ./fly_pt2.py gene_names.txt ~/data/results/stringtie/SRR072893/t_data.ctab include
    Run and exclude no match lines
    ./fly_pt2.py gene_names.txt ~/data/results/stringtie/SRR072893/t_data.ctab ignore
"""

#creating dictionary from argument 1
#comparing c_tab file to dictionary 

import sys

dict={}
for line in open(sys.argv[1]):
    fields=line.strip().split()
    dict[fields[0]] = fields[1]

for line in open(sys.argv[2]):
    fields=line.strip().split("\t")
    if fields[8] in dict:
        uniprotID = dict[fields[8]]
        print(line.rstrip("\r\n") + "\t" + uniprotID)
    else:
        if sys.argv[3] == 'ignore':
            pass
        elif sys.argv[3] == 'include':    
            print(line.rstrip("\r\n") + "\t" + 'found no match')
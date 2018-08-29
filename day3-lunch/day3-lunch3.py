#!/usr/bin/env python3

import sys

f = open(sys.argv[1])
find_pos = 21378950
shortest_dist = 10**10
closest_gene = "error"


for i, line in enumerate(f):
    if line.startswith ("#"):
        continue
    fields=line.rstrip("\r\n").split()
    if "gene" == fields[2] and fields[0] == "3R" and '\"protein_coding\";':
        my_dist = 0
        if find_pos < int(fields[3]):
            my_dist = int(fields[3]) - find_pos
        elif find_pos > int(fields[4]):
            my_dist = find_pos - int(fields[4])
        if shortest_dist > my_dist:
            shortest_dist = my_dist
            closest_gene = fields[13]
print(closest_gene, shortest_dist)
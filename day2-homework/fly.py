#!/usr/bin/env python3

#extract 2 columns from fly doc

import sys

f = open(sys.argv[1])

for i, line in enumerate( f ):
    if "DROME" and "FBgn" in line:
        fields= line.rstrip("\r\n").split()
        print(fields[3], "\t", fields[2])
      

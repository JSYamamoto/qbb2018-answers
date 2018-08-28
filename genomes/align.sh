#!/bin/bash

/Users/cmdb/qbb2018-answers/genomes $ grep -v "^@" SRR072893.sam | grep -v 2110000 | cut -f 3 | head -n 100000 | sort | uniq -c


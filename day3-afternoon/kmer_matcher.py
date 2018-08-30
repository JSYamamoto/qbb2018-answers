#!/usr/bin/env python3

import sys
import fasta


target_sequence = open(sys.argv[1])
query_sequence = open(sys.argv[2])

reader = fasta.FASTAReader(query_sequence)

kmers = {}

k = int(sys.argv[3])

for ident, sequence in reader:
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = [i]
        else:
            kmers[kmer].append(i)
#        else:
#            kmers[kmer] += 1

reader = fasta.FASTAReader(target_sequence)

for ident, sequence in reader:
    for i in range( 0, len(sequence) - k ):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            for key in range(len(kmers[kmer])):
                print(ident, i, kmers[kmer][key], kmer)

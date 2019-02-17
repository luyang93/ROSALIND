#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : cons.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


import numpy as np
from Bio import SeqIO


def main():
    file = 'input/rosalind_cons.txt'
    with open(file) as f:
        seqs = []
        cons = []
        records = list(SeqIO.parse(f, "fasta"))
        for i in range(len(records)):
            seqs.append(' '.join(str(records[i].seq)).split())
        array_seqs = np.array(seqs)
        position_count = np.zeros(shape=(4, array_seqs.shape[1]), dtype=int)
        for i in range(array_seqs.shape[1]):
            array = array_seqs[:, i]
            unique, counts = np.unique(array, return_counts=True)
            base_count = dict(zip(unique, counts))
            j = 0
            cons.append(max(base_count.items(), key=lambda x: x[1])[0])
            for key in ['A', 'C', 'G', 'T']:
                if key in base_count:
                    position_count[j, i] = base_count[key]
                    j += 1
                else:
                    j += 1
    print(''.join(cons))
    j = 0
    for i in ['A', 'C', 'G', 'T']:
        print(i + ': ' + ' '.join(str(e) for e in position_count[j]))
        j += 1


if __name__ == "__main__":
    main()

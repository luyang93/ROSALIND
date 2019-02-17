#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : lcsm.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


import numpy as np
from Bio import SeqIO


def matrix(seq1, seq2):
    matrix_record = np.zeros([len(seq1) + 1, len(seq2) + 1], dtype=np.int64)
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                matrix_record[i + 1, j + 1] = matrix_record[i, j] + 1
            else:
                matrix_record[i + 1, j + 1] = 0
    return matrix_record


def traceback(matrix_record, seq1):
    location = np.argwhere(matrix_record == np.max(matrix_record))
    length = matrix_record[location[0, 0], location[0, 1]]
    longest = seq1[location[0, 0] - length: location[0, 0]]
    return longest


def main():
    file = 'input/rosalind_lcsm.txt'
    records = list(SeqIO.parse(file, "fasta"))
    shared_motif = str(records[0].seq)
    for i in range(1, len(records)):
        matrix_record = matrix(shared_motif, str(records[i].seq))
        shared_motif = traceback(matrix_record, shared_motif)
    print(shared_motif)


if __name__ == "__main__":
    main()

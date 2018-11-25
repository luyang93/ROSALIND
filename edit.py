#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : edit.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)
import numpy as np

from module.readfasta import readfasta


def edit(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    matrix_record = np.zeros([len1 + 1, len2 + 1], dtype=np.int64)
    matrix_record[0, :] = range(0, len2 + 1)
    matrix_record[:, 0] = range(0, len1 + 1)
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                matrix_record[i, j] = matrix_record[i - 1, j - 1]
            else:
                matrix_record[i, j] = min(
                    matrix_record[i, j - 1] + 1,
                    matrix_record[i - 1, j] + 1,
                    matrix_record[i - 1, j - 1] + 1
                )
    return matrix_record


def main():
    file = 'input/rosalind_edit.txt'
    fasta_seq_dict = readfasta(file)
    keys = list(fasta_seq_dict.keys())
    seq1 = fasta_seq_dict[keys[0]]
    seq2 = fasta_seq_dict[keys[1]]
    dist = edit(seq1, seq2)
    print(dist[-1, -1])


if __name__ == "__main__":
    main()

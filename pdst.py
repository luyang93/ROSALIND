#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : pdst.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)
import numpy as np
from module.readfasta import readfasta
from hamm import hamm


def main():
    file = 'input/rosalind_pdst.txt'
    fasta_seq_dict = readfasta(file)
    seq = [''] * len(fasta_seq_dict)
    i = 0
    for keys in fasta_seq_dict.keys():
        seq[i] = str(fasta_seq_dict[keys])
        i = i + 1
    dist_matrix = np.zeros([len(seq), len(seq)])
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            dist_matrix[i, j] = hamm(seq[i], seq[j]) / len(seq[i])
            dist_matrix[j, i] = dist_matrix[i, j]
    for i in range(len(seq)):
        for j in range(len(seq)):
            print(dist_matrix[i, j], end=' ')
        print('')


if __name__ == "__main__":
    main()

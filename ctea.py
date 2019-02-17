#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : ctea.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)


from edit import edit
from module.readfasta import readfasta


def count(matrix, seq1, seq2, i, j):
    if i == 0 or j == 0:
        return 1
    if (i, j) not in have_counted:
        counts = 0
        if matrix[i][j] == matrix[i - 1][j] + 1:
            counts += count(matrix, seq1, seq2, i - 1, j)
        if matrix[i][j] == matrix[i][j - 1] + 1:
            counts += count(matrix, seq1, seq2, i, j - 1)
        if matrix[i][j] == matrix[i - 1][j - 1] and seq1[i - 1] == seq2[j - 1]:
            counts += count(matrix, seq1, seq2, i - 1, j - 1)
        if matrix[i][j] == matrix[i - 1][j - 1] + 1 and seq1[i - 1] != seq2[j - 1]:
            counts += count(matrix, seq1, seq2, i - 1, j - 1)
        have_counted[(i, j)] = counts % (2 ** 27 - 1)

    return have_counted[(i, j)]


def main():
    file = 'input/rosalind_ctea.txt'
    fasta_seq_dict = readfasta(file)
    keys = list(fasta_seq_dict.keys())
    seq1 = fasta_seq_dict[keys[0]]
    seq2 = fasta_seq_dict[keys[1]]
    dist = edit(seq1, seq2)
    count_num = count(dist, seq1, seq2, len(seq1), len(seq2))
    print(count_num)


if __name__ == "__main__":
    have_counted = {}
    main()

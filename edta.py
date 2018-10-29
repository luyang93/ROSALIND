#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : edta.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)
from module.readfasta import readfasta
from edit import edit

def trace(dist, seq1, seq2):
    i = len(seq1)
    j = len(seq2)
    seq1_edit = []
    seq2_edit = []
    while dist[i, j] != 0:
        if seq1[i - 1] == seq2[j - 1]:
            i -= 1
            j -= 1
            seq1_edit.append(seq1[i])
            seq2_edit.append(seq2[j])
        else:
            if dist[i - 1, j - 1] == dist[i, j] - 1:
                i -= 1
                j -= 1
                seq1_edit.append(seq1[i])
                seq2_edit.append(seq2[j])
            if dist[i - 1, j] == dist[i, j] - 1:
                i -= 1
                seq1_edit.append(seq1[i])
                seq2_edit.append('-')
            if dist[i, j - 1] == dist[i, j] - 1:
                j -= 1
                seq1_edit.append('-')
                seq2_edit.append(seq2[j])
    seq1_edit = seq1[0:i] + ''.join(seq1_edit[::-1])
    seq2_edit = seq2[0:j] + ''.join(seq2_edit[::-1])
    return seq1_edit, seq2_edit


def main():
    file = 'input/rosalind_edit.txt'
    fasta_seq_dict = readfasta(file)
    keys = list(fasta_seq_dict.keys())
    seq1 = fasta_seq_dict[keys[0]]
    seq2 = fasta_seq_dict[keys[1]]
    dist = edit(seq1, seq2)
    print(dist[-1, -1])
    (seq1_edit, seq2_edit) = trace(dist, seq1, seq2)
    print(seq1_edit)
    print(seq2_edit)

if __name__ == "__main__":
    main()
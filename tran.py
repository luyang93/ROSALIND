#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : tran.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)
from module.readfasta import readfasta


def main():
    file = 'input/rosalind_tran.txt'
    fasta_seq_dict = readfasta(file)
    keys = list(fasta_seq_dict.keys())
    seq1 = fasta_seq_dict[keys[0]]
    seq2 = fasta_seq_dict[keys[1]]
    transitions = [set('AG'), set('CT')]
    transversions = [set('AC'), set('GT'), set('AT'), set('CG')]
    transition_sum = 0
    transversion_sum = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            pair = {seq1[i], seq2[i]}
            if pair in transitions:
                # print(pair)
                transition_sum += 1
            if pair in transversions:
                # print(pair)
                transversion_sum += 1
    print(transition_sum / transversion_sum)


if __name__ == "__main__":
    main()

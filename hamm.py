#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : hamm.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)


def hamm(seq1, seq2):
    hamming_distance = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            hamming_distance += 1
    return hamming_distance


def main():
    file = 'input/rosalind_hamm.txt'
    with open(file) as f:
        seq1 = f.readline()
        seq2 = f.readline()
    hamming_distance = hamm(seq1, seq2)
    print(hamming_distance)


if __name__ == "__main__":
    main()

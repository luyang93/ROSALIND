#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : revp.py
# @Date    : 2019-02-17
# @Author  : luyang(luyang@novogene.com)


from Bio.Seq import Seq

from module.readfasta import readfasta


def is_palindrome(seq):
    return seq == seq.reverse_complement()


def main():
    file = 'input/rosalind_revp.txt'
    reads = readfasta(file)
    for name in reads:
        seq = Seq(reads[name])
        for i in range(4, 13, 2):
            for j in range(0, len(seq) - i + 1):
                if is_palindrome(seq[j:j + i]):
                    print(j + 1, i)


if __name__ == "__main__":
    main()

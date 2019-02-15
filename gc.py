#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : gc.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)
from module.readfasta import readfasta


def main():
    file = 'input/rosalind_gc.txt'
    reads = readfasta(file)
    name_gc = {}
    for read in reads:
        sequence = reads[read]
        name_gc[read] = (sequence.count('G') + sequence.count('C')) / len(sequence)
    result = max(zip(name_gc.values(), name_gc.keys()))
    print(result[1], '\n', result[0] * 100, sep='')


if __name__ == "__main__":
    main()

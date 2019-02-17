#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : pmch.py
# @Date    : 2019-02-17
# @Author  : luyang(luyang@novogene.com)


from math import factorial

from module.readfasta import readfasta


def main():
    file = 'input/rosalind_pmch.txt'
    reads = readfasta(file)
    for name in reads:
        seq = reads[name]
        if len(seq) % 2 == 0:
            AU_edges = seq.count('A')
            CG_edges = seq.count('C')
            print(factorial(AU_edges) * factorial(CG_edges))


if __name__ == "__main__":
    main()

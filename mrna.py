#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : mrna.py
# @Date    : 2019-02-16
# @Author  : luyang(luyang@novogene.com)


from Bio.Data import CodonTable


def main():
    file = 'input/rosalind_mrna.txt'
    codon = CodonTable.standard_dna_table
    pro_rna = {}
    for k, v in codon.forward_table.items():
        if v in pro_rna:
            pro_rna[v] += 1
        else:
            pro_rna[v] = 1
    count_rna = 1
    with open(file) as f:
        line = f.readline().strip()
        for base in line:
            count_rna *= pro_rna[base] % 1000000
    print(count_rna * 3 % 1000000)


if __name__ == "__main__":
    main()

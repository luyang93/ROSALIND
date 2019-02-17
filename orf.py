#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : orf.py
# @Date    : 2019-02-17
# @Author  : luyang(luyang@novogene.com)


import re

from Bio.Seq import Seq

from module.readfasta import readfasta


def find_orf(seq):
    position = []
    for i in pattern.finditer(seq):
        start_position = i.start()
        j = start_position
        while j < len(seq):
            mrna = seq[j:j + 3]
            if mrna in stop_codons:
                flag = 1
                break
            else:
                flag = 0
            j += 3
        if flag:
            tmp = Seq(seq[start_position:j + 3]).translate(stop_symbol='')
            prot[str(tmp)] = ''


def main():
    file = 'input/rosalind_orf.txt'
    reads = readfasta(file)
    for name in reads:
        seq = reads[name]
        find_orf(seq)
        seq = str(Seq(reads[name]).reverse_complement())
        find_orf(seq)
    for key in prot.keys():
        print(key)


if __name__ == "__main__":
    pattern = re.compile('(?=(ATG))')
    stop_codons = ['TAG', 'TGA', 'TAA']
    prot = {}
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : sseq.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


from Bio import SeqIO


def main():
    # 用Biopython读取fasta
    file = 'input/rosalind_sseq.txt'
    with open(file) as f:
        records = list(SeqIO.parse(f, "fasta"))
    s = str(records[0].seq)
    t = str(records[1].seq)

    position = 0
    log = []
    for i in t:
        index = s[position:].find(i)
        position += index + 1
        log.append(position)

    print(" ".join(map(str, log)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : splc.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq


def main():
    file = 'input/rosalind_splc.txt'
    seq = ''
    for seq_record in SeqIO.parse(file, "fasta"):
        if seq:
            exon = str(seq_record.seq)
        else:
            seq = str(seq_record.seq)
            continue
        position = seq.find(exon)
        seq = seq[0:position] + seq[position + len(exon):]
    print(Seq(seq, IUPAC.unambiguous_dna).translate())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : readfasta.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)

def readfasta(file):
    fasta_seq_dict = {}
    with open(file) as f:
        fasta_name = ''
        fasta_seq = ''
        for line in f.readlines():
            if ">" in line:
                fasta_name = line.lstrip('>').rstrip('\n')
                fasta_seq = ''
            else:
                fasta_seq += line.rstrip('\n')
                fasta_seq_dict[fasta_name] = fasta_seq
    return fasta_seq_dict


def main():
    pass


if __name__ == '__main__':
    main()

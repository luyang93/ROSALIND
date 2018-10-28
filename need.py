#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : need.py
# @Date    : 18-10-28
# @Author  : luyang(luyang@novogene.com)
import os
from Bio import Entrez
from Bio.Emboss.Applications import NeedleCommandline
from Bio import SeqIO
from Bio import AlignIO
import subprocess


def main():
    os.environ['http_proxy'] = 'http://127.0.0.1:1081'
    file = 'input/rosalind_need.txt'
    with open(file) as f:
        ids = f.readline().strip().split()
    Entrez.email = '510426762@qq.com'  # Always tell NCBI who you are
    Entrez.api_key = 'd75c9c53e469a62dc79517fb9e47b3b18e08'
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))
    handle.close()
    with open('seq1.fasta', 'w') as f:
        SeqIO.write(records[0], f, 'fasta')
    with open('seq2.fasta', 'w') as f:
        SeqIO.write(records[1], f, 'fasta')
    # print('>', end='')
    # print(records[0].description)
    # print(records[0].seq)
    # print('>', end='')
    # print(records[1].description)
    # print(records[1].seq)
    needle_cline = NeedleCommandline()
    # needle_cline.program_name=subprocess.getoutput('which needle')
    needle_cline.asequence = 'seq1.fasta'
    needle_cline.bsequence = 'seq2.fasta'
    needle_cline.gapopen = 10
    needle_cline.gapextend = 1
    needle_cline.endopen = 10
    needle_cline.endextend = 1
    needle_cline.endweight = True
    needle_cline.outfile = 'output/needle.txt'
    child = subprocess.Popen(str(needle_cline), shell=True)
    child.wait()
    os.remove('seq1.fasta')
    os.remove('seq2.fasta')
    align = AlignIO.read('output/needle.txt', 'emboss')
    print(align.annotations['score'])
    os.remove('output/needle.txt')


if __name__ == "__main__":
    main()

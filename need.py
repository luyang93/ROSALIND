#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : need.py
# @Date    : 18-10-28
# @Author  : luyang(luyang@novogene.com)


import os
import subprocess

from Bio import AlignIO
from Bio import Entrez
from Bio import SeqIO
from Bio.Emboss.Applications import NeedleCommandline


def main():
    os.environ['http_proxy'] = 'http://localhost:1081'
    os.environ['PATH'] += ':/home/luyang/miniconda3/envs/PCC/bin'
    file = 'input/rosalind_need.txt'
    with open(file) as f:
        ids = f.readline().strip().split()
    Entrez.email = '510426762@qq.com'  # Always tell NCBI who you are
    Entrez.api_key = 'd75c9c53e469a62dc79517fb9e47b3b18e08'
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta')
    records = list(SeqIO.parse(handle, 'fasta'))
    # with open('output/seq1.fasta', 'w') as f:
    #     SeqIO.write(records[0], f, 'fasta')
    # with open('output/seq2.fasta', 'w') as f:
    #     SeqIO.write(records[1], f, 'fasta')
    handle.close()
    needle_cline = NeedleCommandline()
    needle_cline.asequence = 'asis:' + str(records[0].seq)
    needle_cline.bsequence = 'asis:' + str(records[1].seq)
    # needle_cline.asequence = 'output/seq1.fasta'
    # needle_cline.bsequence = 'output/seq2.fasta'
    needle_cline.gapopen = 10
    needle_cline.gapextend = 1
    needle_cline.endopen = 10
    needle_cline.endextend = 1
    needle_cline.endweight = True
    needle_cline.outfile = 'stdout'
    child = subprocess.Popen([str(needle_cline)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = child.stdout.read().decode('utf-8')
    with open('output/needle.txt', 'w') as f:
        f.writelines(result)
    with open('output/needle.txt', 'r') as f:
        align = AlignIO.read(f, 'emboss')
    print(align.annotations['score'])
    # os.remove('output/seq1.fasta')
    # os.remove('output/seq2.fasta')
    os.remove('output/needle.txt')


if __name__ == "__main__":
    main()

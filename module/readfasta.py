#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : readfasta.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)

def readfasta(file):
    name_seq = {}
    with open(file) as f:
        name = ''
        seq = []
        for line in f.readlines():
            if line.startswith('>'):
                name_seq[name] = ''.join(seq)
                name = line.lstrip('>').rstrip('\n')
                seq = []
            else:
                seq.append(line.strip('\n'))
    name_seq[name] = ''.join(seq)
    del name_seq['']
    return name_seq

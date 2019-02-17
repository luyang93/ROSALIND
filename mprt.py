#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : mprt.py
# @Date    : 2019-02-16
# @Author  : luyang(luyang@novogene.com)


import re

from Bio import ExPASy
from Bio import SeqIO


def main():
    file = 'input/rosalind_mprt.txt'
    with open(file) as f:
        for id in f.readlines():
            handle = ExPASy.get_sprot_raw(id.strip())
            seq_record = SeqIO.read(handle, "swiss")
            # ?= 零宽断言
            pattern = re.compile('(?=(N[^P][ST][^P]))')
            positions = pattern.finditer(str(seq_record.seq))
            position = []
            for i in positions:
                position.append(i.start() + 1)
            if position:
                print(id.strip())
                print(' '.join(map(str, position)))


if __name__ == "__main__":
    main()

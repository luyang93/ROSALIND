#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : prot.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)
from Bio.Seq import Seq


def main():
    file = 'input/rosalind_prot.txt'
    with open(file) as f:
        line = f.readline().strip()
        my_seq = Seq(line)
        print(my_seq.translate())


if __name__ == "__main__":
    main()

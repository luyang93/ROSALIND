#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : dna.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_dna.txt'
    with open(file) as f:
        line = f.readline().strip()
        print(*map(line.count, 'ACGT'))


if __name__ == "__main__":
    main()

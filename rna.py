#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : rna.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_rna.txt'
    with open(file) as f:
        line = f.readline().strip()
        print(line.replace('T', 'U'))


if __name__ == "__main__":
    main()

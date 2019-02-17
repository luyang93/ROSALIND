#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : grph.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


from module.readfasta import readfasta


def main():
    file = 'input/rosalind_grph.txt'
    reads = readfasta(file)
    for i in reads:
        for j in reads:
            if i == j:
                continue
            elif reads[i][-3:] == reads[j][:3]:
                print(i, j)


if __name__ == "__main__":
    main()

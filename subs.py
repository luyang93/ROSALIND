#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : subs.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)

def main():
    file='input/rosalind_subs.txt'
    with open(file) as f:
        seq1 = f.readline().strip()
        seq2 = f.readline().strip()
        i = seq1.find(seq2)
        while i != -1:
            print(i+1,end=' ')
            i = seq1.find(seq2, i + 1)


if __name__ == "__main__":
    main()
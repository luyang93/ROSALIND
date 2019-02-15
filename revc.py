#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : revc.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)

def main():
    file = 'input/rosalind_revc.txt'
    with open(file) as f:
        line = f.readline().strip()
        trans = str.maketrans('ATCG', 'TAGC')
        print(line.translate(trans)[::-1])


if __name__ == "__main__":
    main()

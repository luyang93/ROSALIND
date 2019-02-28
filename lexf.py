#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : lexf.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


from itertools import product


def main():
    file = 'input/rosalind_lexf.txt'
    with open(file) as f:
        s = f.readline().strip().split()
        n = int(f.readline().strip())
        products = product(s, repeat=n)
    for i in products:
        print(''.join(i))


if __name__ == "__main__":
    main()

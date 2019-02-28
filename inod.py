#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : inod.py
# @Date    : 2019-02-27
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_inod.txt'
    with open(file) as f:
        n = int(f.readline())
    print(n - 2)

if __name__ == "__main__":
    main()
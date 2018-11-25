#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : INI4.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_ini4.txt'
    with open(file) as f:
        s, e = map(int, f.readline().split())
    summation = 0
    for i in range(s, e + 1):
        if i % 2:
            summation += i
    print(summation)


if __name__ == "__main__":
    main()

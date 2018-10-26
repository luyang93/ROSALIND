#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : INI2.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)

def main():
    file = 'input/rosalind_ini2.txt'
    with open(file) as f:
        a, b = map(int, f.readline().split())
    print(a ** 2 + b ** 2)


if __name__ == "__main__":
    main()

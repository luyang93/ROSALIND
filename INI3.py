#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : INI3.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_ini3.txt'
    with open(file) as f:
        string = f.readline()
        s1, e1, s2, e2 = map(int, f.readline().split())
    print(string[s1:e1 + 1], string[s2:e2 + 1])


if __name__ == "__main__":
    main()

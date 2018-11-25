#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : INI5.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_ini5.txt'
    with open(file) as f:
        i = 1
        for line in f.readlines():
            if not i % 2:
                print(line, end='')
            i += 1


if __name__ == "__main__":
    main()

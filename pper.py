#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : pper.py
# @Date    : 2019-02-17
# @Author  : luyang(luyang@novogene.com)


from math import factorial


def main():
    file = 'input/rosalind_pper.txt'
    with open(file) as f:
        n, k = map(int, f.readline().strip().split())
        print(int(factorial(n) / factorial(n - k) % 1000000))


if __name__ == "__main__":
    main()

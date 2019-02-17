#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : perm.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


from itertools import permutations
from math import factorial


def main():
    names = ['John', 'Tom', 'Alice', 'Ben']
    file = 'input/rosalind_perm.txt'
    with open(file) as f:
        num = int(f.readline())
        nums = ''.join(map(str, list(range(1, num + 1))))
        combs = permutations(nums, num)
        print(factorial(num))
        print('\n'.join((map(lambda comb: ' '.join(comb), combs))))


if __name__ == "__main__":
    main()

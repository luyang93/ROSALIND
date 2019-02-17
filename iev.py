#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : iev.py
# @Date    : 2019-02-16
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_iev.txt'
    with open(file) as f:
        num_couples = list(map(int, f.readline().strip().split()))
        num_expected = num_couples[0] * 1 + num_couples[1] * 1 + num_couples[2] * 1 + num_couples[3] * 3 / 4 + num_couples[4] * 1 / 2 + num_couples[0] * 0
        print(num_expected * 2)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : fib.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)

import numpy as np
from prettytable import PrettyTable


def fib(month, produce, young):
    rabbits = np.zeros([month, 2])
    # 第一个月的起始状况，1对young，0对mature
    rabbits[0, 0] = young
    rabbits[0, 1] = 0

    for i in range(1, month):
        # 次月young <- 上月mature * produce
        rabbits[i, 0] = produce * rabbits[i - 1, 1]
        # 次月mature <- 上月young + 上月mature
        rabbits[i, 1] = rabbits[i - 1].sum()
    # 返回每个月的状况
    return rabbits


def main():
    file = 'input/rosalind_fib.txt'
    with open(file) as f:
        line = f.readline()
    young = 1
    month = int(line.split()[0])
    produce = int(line.split()[1])
    rabbits = fib(month, produce, young)
    pt = PrettyTable(['month', 'young', 'mature', 'total'])
    for i in range(month):
        pt.add_row([i + 1, rabbits[i, 0], rabbits[i, 1], rabbits[i].sum()])
    print(pt)


if __name__ == "__main__":
    main()

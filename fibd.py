#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : fibd.py
# @Date    : 2019-02-16
# @Author  : luyang(luyang@novogene.com)
import numpy as np


def fibd(lastmonth, livemonth, young):
    rabbits = np.zeros(([lastmonth, livemonth]), dtype='uint64')
    # 初始化第一个月数据,lastmonth = 5
    # 初始兔子young对，1:livemonth-1都为0
    rabbits[0, 0] = young
    rabbits[0, 1:livemonth] = 0

    # print(rabbits[0])
    for i in range(1, lastmonth):
        # young等于上个月除young之外所有兔子之和
        rabbits[i, 0] = rabbits[i - 1, 1:livemonth].sum()
        # 次月数据等于上月数据享有偏移1
        rabbits[i, 1:livemonth] = rabbits[i - 1, 0:livemonth - 1]
        # print(rabbits[i])
    return rabbits


def main():
    file = 'input/rosalind_fibd.txt'
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            young = 1
            last_month = int(line.split()[0])
            live_month = int(line.split()[1])
            rabbit = fibd(last_month, live_month, young)
            d = int(rabbit[last_month - 1, :].sum())
            print(d)


if __name__ == "__main__":
    main()

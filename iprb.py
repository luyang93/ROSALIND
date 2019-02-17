#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : iprb.py
# @Date    : 2019-02-15
# @Author  : luyang(luyang@novogene.com)


def main():
    file = 'input/rosalind_iprb.txt'
    with open(file) as f:
        k, m, n = map(int, f.readline().split())
        t = k + m + n
        pk = k / t
        pm = m / t
        pn = n / t
        prob = 1
        # 两个纯合隐性
        prob -= pn * (n - 1) / (t - 1)
        # 一个杂合，一个纯合隐形
        prob -= 2 * pn * (m / (t - 1)) * 0.5
        # 两个杂合
        prob -= pm * ((m - 1) / (t - 1)) * 0.25
        print(prob)


if __name__ == "__main__":
    main()

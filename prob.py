#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : prob.py
# @Date    : 2019-02-17
# @Author  : luyang(luyang@novogene.com)


from math import log10


def main():
    file = 'input/rosalind_prob.txt'
    with open(file) as f:
        seq = f.readline().strip()
        for GC_content in map(float, f.readline().strip().split()):
            base_prob = {'A': 0.5 - GC_content / 2, 'T': 0.5 - GC_content / 2, 'C': GC_content / 2, 'G': GC_content / 2}
            log_probability = log10(1)
            for i in seq:
                log_probability += log10(base_prob[i])
            print(log_probability, end=' ')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : ba10a.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)


import numpy as np


def main():
    file = 'input/rosalind_ba10a.txt'
    with open(file) as f:
        lines = f.readlines()
    hidden_sequence = lines[0].strip()
    hiddens = lines[2].strip().split('\t')
    start_probability = 0.5
    probability = start_probability
    transition_matrix = np.zeros([len(hiddens), len(hiddens)])
    for i in range(len(hiddens)):
        transition_matrix[i:, ] = lines[i + 5].strip().split('\t')[1:]
    for i in range(0, len(hidden_sequence) - 1):
        probability *= transition_matrix[hiddens.index(hidden_sequence[i]), hiddens.index(hidden_sequence[i + 1])]
    print(probability)


if __name__ == "__main__":
    main()

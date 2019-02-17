#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : ba10b.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)


import numpy as np


def main():
    file = 'input/rosalind_ba10b.txt'
    with open(file) as f:
        lines = f.readlines()
    observation_sequence = lines[0].strip()
    observation = lines[2].strip().split('\t')
    hidden_sequence = lines[4].strip()
    hiddens = lines[6].strip().split('\t')
    start_probability = 1
    probability = start_probability
    emission_matrix = np.zeros([len(hiddens), len(observation)])
    for i in range(len(hiddens)):
        emission_matrix[i:, ] = lines[i + 9].strip().split('\t')[1:]

    for i in range(len(observation_sequence)):
        probability *= emission_matrix[hiddens.index(hidden_sequence[i]), observation.index(observation_sequence[i])]
    print(probability)


if __name__ == "__main__":
    main()

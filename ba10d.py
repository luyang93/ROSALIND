#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : ba10d.py
# @Date    : 18-10-30
# @Author  : luyang(luyang@novogene.com)


import numpy as np


def likelihood(observations, hiddens, observation_sequence, transition_matrix, emission_matrix):
    # init
    hiddens_prob = np.zeros([len(observation_sequence), len(hiddens)], dtype=np.float128)
    observations_prob = np.zeros([len(observation_sequence), len(hiddens)], dtype=np.float128)
    # 0时刻
    index = observations.index(observation_sequence[0])
    # 隐藏状态的概率
    hiddens_prob[0, :] = np.array([1 / len(hiddens)] * len(hiddens))
    # 分别从hidden放射到observation[index]的概率
    observations_prob[0, :] = hiddens_prob[0, :] * emission_matrix[:, index]

    for i in range(1, len(observation_sequence)):
        index = observations.index(observation_sequence[i])
        hiddens_prob[i, :] = np.matmul(observations_prob[i - 1, :], transition_matrix)
        observations_prob[i, :] = np.multiply(hiddens_prob[i, :], emission_matrix[:, index].T)

    return np.sum(observations_prob[-1, :])


def main():
    file = 'input/rosalind_ba10d.txt'
    with open(file) as f:
        lines = f.readlines()
    # 读取数据,观测
    observations = lines[2].strip().split('\t')
    # 读取数据,状态
    hiddens = lines[4].strip().split('\t')
    # 读取数据,观测时间序列
    observation_sequence = lines[0].strip()
    # 读取数据,转移矩阵
    transition_matrix = np.zeros([len(hiddens), len(hiddens)], dtype=np.float128)
    for i in range(len(hiddens)):
        transition_matrix[i, :] = lines[i + 7].strip().split('\t')[1:]
    # 读取数据,放射矩阵
    emission_matrix = np.zeros([len(hiddens), len(observations)], dtype=np.float128)
    for i in range(len(hiddens)):
        emission_matrix[i, :] = lines[i + len(hiddens) + 9].strip().split('\t')[1:]

    prob = likelihood(observations, hiddens, observation_sequence, transition_matrix, emission_matrix)
    print(prob)


if __name__ == "__main__":
    main()

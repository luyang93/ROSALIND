#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : ba10c.py
# @Date    : 18-10-29
# @Author  : luyang(luyang@novogene.com)
import numpy as np


def viterbi(observations, hiddens, start_probability, observation_sequence, transition_matrix, emission_matrix):
    # 维特比算法
    # 输入:观测状态,隐藏状态,起始概率,观测状态时间序列,转移矩阵,放射矩阵
    # 输出,隐藏状态时间序列
    T1 = np.zeros([len(hiddens), len(observation_sequence)])
    T2 = np.zeros(T1.shape, dtype=int)
    # 获取观测状态编号,方便矩阵使用
    index = observations.index(observation_sequence[0])
    T1[:, 0] = start_probability * emission_matrix[:, index]
    # T1,取max
    # A → A → x(max)    A   A
    #   ↗                  ↘
    # B   B               B → B → x(max)
    # T2,i-1时,A/B → A → x,A/B → B → x,分别哪一个可能性最大,
    # [ [..., 0, ...],
    #   [..., 1, ...] ]
    for i in range(1, len(observation_sequence)):
        index = observations.index(observation_sequence[i])
        for j in range(len(hiddens)):
            T1[j, i] = np.max(T1[:, i - 1] * transition_matrix[:, j] * emission_matrix[j, index])
            T2[j, i] = np.argmax(T1[:, i - 1] * transition_matrix[:, j] * emission_matrix[j, index])
    # path:确定最大可能性路径
    path = np.argmax(T1, axis=0)
    # hidden_sequence:隐藏状态时间序列
    hidden_sequence = [hiddens[i] for i in path]
    # 回溯
    for i in range(len(observation_sequence) - 1, 0, -1):
        path[i - 1] = T2[path[i], i]
        hidden_sequence[i - 1] = hiddens[path[i - 1]]
    return hidden_sequence


def main():
    file = 'input/rosalind_ba10c.txt'
    with open(file) as f:
        lines = f.readlines()
    # 读取数据,观测状态
    observations = lines[2].strip().split('\t')
    # 读取数据,隐藏状态
    hiddens = lines[4].strip().split('\t')
    # 读取数据,观测状态时间序列
    observation_sequence = lines[0].strip()
    # 读取数据,转移矩阵
    transition_matrix = np.zeros([len(hiddens), len(hiddens)])
    for i in range(len(hiddens)):
        transition_matrix[i, :] = lines[i + 7].strip().split('\t')[1:]
    # 读取数据,放射矩阵
    emission_matrix = np.zeros([len(hiddens), len(observations)])
    for i in range(len(hiddens)):
        emission_matrix[i, :] = lines[i + len(hiddens) + 9].strip().split('\t')[1:]
    # 初始化起始概率
    # start_probability = [1/len(hiddens)]*len(hiddens)
    start_probability = [1] * len(hiddens)
    # 维特比算法
    hidden_sequence = viterbi(observations, hiddens, start_probability, observation_sequence, transition_matrix, emission_matrix)
    print(''.join(hidden_sequence))


if __name__ == "__main__":
    main()

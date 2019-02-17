#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : long.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


import networkx as nx

from module.readfasta import readfasta


def compare_reads(r1, r2):
    for i in range(len(r1)):
        length = len(r1) - i
        if r1[i:length + i] == r2[:length]:
            if length > len(r2) / 2:
                return length
            else:
                continue
    return 0


def main():
    file = 'input/rosalind_long.txt'
    reads = readfasta(file)
    G = nx.DiGraph()
    for name in reads:
        G.add_node(name)
    for i in reads:
        for j in reads:
            if i == j:
                continue
            else:
                w = compare_reads(reads[i], reads[j])
                if w:
                    G.add_edge(i, j, weight=w)
    seq = []
    node_list = nx.dag_longest_path(G)
    seq.append(reads[node_list[0]])
    for i in range(1, len(node_list)):
        src = node_list[i - 1]
        dst = node_list[i]
        w = G.get_edge_data(src, dst)['weight']
        seq.append(reads[dst][w:])
    print(seq)
    print(''.join(seq))


if __name__ == "__main__":
    main()

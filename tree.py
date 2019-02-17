#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : tree.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


import networkx as nx


def main():
    file = 'input/rosalind_tree.txt'
    with open(file) as f:
        number_nodes = int(f.readline().strip())
        G = nx.Graph()
        line = f.readline()
        while line:
            edge = [int(i) for i in line.strip().split()]
            G.add_edge(edge[0], edge[1])
            line = f.readline()
        # A tree with n nodes has n-1 edges,(every node except the root has an edge to its parent)
        # 每个子node都有一条edge连向父node
        # -1,根node没有edge
        # edges = nodes - 1
        edge_to_add = number_nodes - 1 - G.number_of_edges()
        # nx.draw(G, pos=nx.random_layout(G), node_color = 'b', edge_color = 'r', with_labels = True,font_size = 10, node_size = 10)
        # plt.savefig('1.png')
        print(edge_to_add)
        # print(G.number_of_nodes())
        G.add_nodes_from(list(range(1, number_nodes + 1)))
        # print(G.number_of_nodes())


if __name__ == "__main__":
    main()

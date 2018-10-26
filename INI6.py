#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : INI6.py
# @Date    : 18-10-26
# @Author  : luyang(luyang@novogene.com)

def main():
    file = 'input/rosalind_ini6.txt'
    with open(file) as f:
        line = f.readline()
        words = line.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for keys,values in word_dict.items():
        print(keys,values)

if __name__ == "__main__":
    main()
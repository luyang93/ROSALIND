#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : sign.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


from itertools import product, permutations


def main():
    file = 'input/rosalind_sign.txt'
    with open(file) as f:
        n = int(f.readline().strip())
        numbers = permutations(range(1, n + 1), n)
        signs = product('+-', repeat=n)
        count = 0
        for i in product(numbers, signs, repeat=1):
            for j in range(n):
                if i[1][j] == '+':
                    print(i[0][j], end=' ')
                else:
                    print('-', i[0][j], sep='', end=' ')
            print('')
            count += 1
        print(count)


if __name__ == "__main__":
    main()

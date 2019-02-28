#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : lgis.py
# @Date    : 2019-02-18
# @Author  : luyang(luyang@novogene.com)


def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


def lds(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] > arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


def main():
    file = 'input/rosalind_lgis.txt'
    with open(file) as f:
        n = int(f.readline())
        numbers = list(map(int, f.readline().strip().split()))
    lis_seq = lis(numbers)
    print(' '.join(map(str, lis_seq)))
    lds_seq = lds((numbers))
    print(' '.join(map(str, lds_seq)))


if __name__ == "__main__":
    main()

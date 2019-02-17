#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : lia.py
# @Date    : 2019-02-16
# @Author  : luyang(luyang@novogene.com)


from math import factorial

from scipy.stats import binom


# Binomial_distribution
# f(x) = n!/x!(n-x)!*p^x*(1-p)^(n-x)

def Binomial_distribution(k, n, p):
    return factorial(2 ** k) / factorial(n) / factorial(2 ** k - n) * p ** n * (1 - p) ** (2 ** k - n)


def main():
    file = 'input/rosalind_lia.txt'
    with open(file) as f:
        k, n = map(int, f.readline().strip().split())
    print(1 - binom.cdf(n - 1, 2 ** k, 0.25))

    print('Binomial_distribution')
    probability = 1
    for i in range(1, n):
        probability -= Binomial_distribution(k, i, 1 / 4)
    print(probability)


if __name__ == "__main__":
    main()

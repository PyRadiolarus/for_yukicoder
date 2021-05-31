# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

L, K = map(int, stdin.readline().split())
res = 0

if L % K == 0:
    if (L // K) % 2 == 0:
        res = L // (2 * K) - 1
    else:
        res = L // (2 * K)
else:
    res = L // (2 * K)

print(res*K)
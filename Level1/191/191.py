# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
C = [int(i) for i in stdin.readline().split()]

border = sum(C) / 10
res = 0
for i in range(len(C)):
    cand = C[i]
    if C[i] <= border:
        res += 30
    else:
        pass
print(res)
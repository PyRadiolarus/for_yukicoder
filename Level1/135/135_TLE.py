# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
X = [int(i) for i in stdin.readline().split()]
res = max(X)
for i in range(N):
    p_i = X[i]
    for j in range(1,N):
        p_j = X[j]
        if X[i] == X[j] or i == j:
            pass
        else:
            res = min(res, abs(X[i] - X[j]))
print(res)
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
X = [int(i) for i in stdin.readline().split()]
X.sort()
res = X[N-1]
for i in range(1,N):
    r = X[i] - X[i-1]
    if r == 0:
        pass
    else:
        res = min(res, r)
print(res)
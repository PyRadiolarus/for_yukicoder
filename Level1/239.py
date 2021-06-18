# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
A = [stdin.readline().split() for i in range(N)]
A = list(map(lambda *a: a, *A))
res = []
for i in range(N):
    if A[i].count("nyanpass") == N-1:
        res += [i]

if len(res) == 1:
    print(res[0]+1)
else:
    print(-1)
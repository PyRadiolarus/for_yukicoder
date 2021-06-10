# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, M = map(int, stdin.readline().split())
C = [int(i) for i in stdin.readline().split()]
C.sort()
res = 0
for i in range(N):
    if C[i] > M:
        break
    else:
        M -= C[i]
        res += 1
print(res)
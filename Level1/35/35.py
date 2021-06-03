# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")
from math import floor
N = int(stdin.readline())
TS = [stdin.readline().split() for i in range(N)]

res, miss = 0, 0
for i in range(len(TS)):
    T, S = int(TS[i][0]), str(TS[i][1])
    T_ = floor(12 * T / 1000)
    if T_ >= len(S):
        res += len(S)
    else:
        lost = len(S) - T_
        miss += lost
        res += len(S) - lost
print(res, miss)
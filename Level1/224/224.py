# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

n = int(stdin.readline())
S = list(str(stdin.readline().rstrip()))
T = list(str(stdin.readline().rstrip()))
res = 0
for i in range(n):
    if S[i] != T[i]:
        res += 1
    else:
        pass
print(res)
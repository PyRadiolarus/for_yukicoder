# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
M = int(stdin.readline())

for i in range(M):
    P, Q = map(int, stdin.readline().split())
    if N == P:
        N = Q
    elif N == Q:
        N = P
    else:
        pass
print(N)
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N, H, M, T = map(int, stdin.readline().split())

if N == 1:
    pass
else:
    M = M + (N-1) * T
    if M >= 60:
        d_H, d_M = divmod(M, 60)
        H += d_H
        M = d_M
    else:
        pass
    if H >= 24:
        H = H % 24
    else:
        pass
print(H,M,sep="\n")
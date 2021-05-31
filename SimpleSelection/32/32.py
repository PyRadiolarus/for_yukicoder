# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

L = int(stdin.readline())
M = int(stdin.readline())
N = int(stdin.readline())
res = 0

if N >= 25:
    res_n, mod_n = divmod(N, 25)
    M += res_n
    res += mod_n
else:
    res += N

if M >= 4:
    res_m, mod_m = divmod(M, 4)
    L += res_m
    res += mod_m
else:
    res += M

if L >= 10:
    res += L % 10
else:
    res += L

print(res)
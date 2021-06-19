# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
B = [int(i) for i in stdin.readline().split()]
res = [0] * 100
p = 0
for i, a in enumerate(A):
    if B[i] == 0:
        p += a
    else:
        res[B[i]-1] += a
print("YES" if p >= max(res) else "NO")

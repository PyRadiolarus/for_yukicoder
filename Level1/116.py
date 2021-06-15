# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
res = 0
for i in range(N-2):
    l = A[i:i+3]
    if l[0] != l[2] and (l[1]-l[0]) * (l[1]-l[2]) > 0:
        res += 1
print(res)
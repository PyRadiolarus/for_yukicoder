# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

A, B, C, D = map(int, stdin.readline().split())
res = 0
for i in range(A, B+1):
    for j in range(C, D+1):
        if i != j:res += 1
print(res)
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

K, N, F = map(int, stdin.readline().split())
A = [int(i) for i in stdin.readline().split()]

beans = K * N

for i in range(F):
    age = A[i]
    beans -= age

if beans <= -1:
    print(-1)
else:
    print(beans)
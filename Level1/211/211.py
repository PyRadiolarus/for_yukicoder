# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

K = int(stdin.readline())
m = [4,6,8,9,10,12]
p = [2,3,5,7,11,13]
v = 0
for i in range(6):
    for j in range(6):
        if m[i] * p[j] == K:
            v += 1
if v == 0:
    print(0)
else:
    print(v / 36)
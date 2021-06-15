# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

L = int(stdin.readline())
N = int(stdin.readline())
W = [int(i) for i in stdin.readline().split()]
W.sort()
res = 0
width = 0

for i in range(len(W)):
    width += W[i]
    if L > width:
        res += 1
    elif L == width:
        res += 1
        break
    else:
        pass

print(res)
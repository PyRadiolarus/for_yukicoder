# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
L = [int(i) for i in stdin.readline().split()]
L.sort()
mode, count = 0, 0
for i in range(min(L),max(L)+1):
    lHigh = L.count(i)
    if lHigh == 0:
        pass
    else:
        if count <= lHigh:
            count = lHigh
            mode = i
        else:
            pass
print(mode)
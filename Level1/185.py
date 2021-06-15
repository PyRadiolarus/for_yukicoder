# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
xy = [map(int, stdin.readline().split()) for i in range(N)]
x, y = [list(i) for i in zip(*xy)]
res = -1
for i in range(N):
    square = y[i] - x[i]
    if i == 0:
        sq_ = square
        pass
    else:
        if square != sq_:
            res = -1
            break
        else:
            res = square
            if res <= 0:
                res = -1
                break
print(res)
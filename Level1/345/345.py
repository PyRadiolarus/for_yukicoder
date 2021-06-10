# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

S = str(stdin.readline())
s, f, res = 1000, 1000, 1000
for i in range(len(S)):
    if S[i] == "c":
        s = i
    elif S[i] == "w":
        if f != 1000:
            res = min(res, i - f + 1)
        if s != 1000:
            f = s
if res == 1000:
    res = -1
print(res)
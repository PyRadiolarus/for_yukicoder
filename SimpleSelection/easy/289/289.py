# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

S = list(str(stdin.readline().rstrip()))
res = 0
for i in range(len(S)):
    TF = S[i].isdecimal()
    if TF:
        res += int(S[i])
    else:
        pass

print(res)
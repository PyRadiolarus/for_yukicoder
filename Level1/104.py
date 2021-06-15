# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = str(stdin.readline().rstrip())
res = 1
for i in range(len(S)):
    drct = S[i]
    if drct == "L":
        Num = 2 * res
    elif drct == "R":
        Num = 2 * res + 1
    res = Num
print(res)
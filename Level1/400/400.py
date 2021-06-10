# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

S = str(stdin.readline().rstrip())
resl = []
for i in reversed(S):
    if i == "<":
        c = ">"
    else:
        c = "<"
    resl.append(c)
res = "".join(resl)
print(res)

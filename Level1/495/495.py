# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

S = [str(i) for i in stdin.readline().split(")")]
if S[0] == "(^^*":
    j = 1
elif S[0] == "(*^^":
    j = 2
else:
    j = 0

if j == 1 or j == 2:
    L = S.count("(^^*")
    R = S.count("(*^^")
else:
    L, R = 0, 0
print(L, "", R)

# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = stdin.readline().rstrip()
s = int(N)
for i in range(s):
    print(N * s)
    s -= 1
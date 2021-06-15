# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = stdin.readline().rstrip()
full = "yukicoder"
for i in range(len(S)):
    if S[i] != full[i]:
        print(full[i])
    else:
        pass
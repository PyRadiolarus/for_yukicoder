# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S, t, u = map(str, stdin.readline().split())
t, u = int(t), int(u)
if t == u:
    if t == 0:
        print(S[1:])
    elif t == len(S) - 1:
        print(S[:-1])
    else:
        print(S[:t] + S[t+1:])
elif t < u:
    print(S[:t] + S[t+1:u] + S[u+1:])
else:
    print(S[:u] + S[u+1:t] + S[t+1:])
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
S = [str(i) for i in stdin.readline().split()]
T = [str(i) for i in stdin.readline().split()]
for i in range(N):
    if S[i] != T[i]:
        print(i+1, S[i], T[i], sep="\n")
        break
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
S = [stdin.readline().rstrip() for i in range(N)]
print("".join(S))
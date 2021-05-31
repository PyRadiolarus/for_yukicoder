# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
K = int(stdin.readline())
n = [int(stdin.readline()) for i in range(N)]
print(max(n) - min(n))
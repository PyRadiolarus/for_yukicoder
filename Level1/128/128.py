# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
M = int(stdin.readline())
res = 0

bill = N // 1000
res = 1000 * (bill // M)
print(res)
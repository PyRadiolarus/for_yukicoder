# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline().rstrip())
res = 0
cookie = 1

while cookie < N:
    cookie = 2 * cookie
    res += 1

print(res)
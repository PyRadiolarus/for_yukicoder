# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

a, b = map(int, stdin.readline().split())
q, mod = divmod(b, a)

if mod > 0:
    q += 1
else:
    pass

print(q)
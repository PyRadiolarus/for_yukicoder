# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

A, B = map(int, stdin.readline().split())
q = B / A
if q.is_integer():
    print(int(q))
else:
    print("NO")
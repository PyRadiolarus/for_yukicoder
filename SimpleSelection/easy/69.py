# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

A = str(stdin.readline().rstrip())
B = str(stdin.readline().rstrip())

A = sorted(A)
B = sorted(B)

if A == B:
    print("YES")
else:
    print("NO")
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

a, b = map(int, stdin.readline().split())
s = b - a
if s == 0:
    print("0")
elif s < 0:
    print(str(s))
else:
    print("+"+ str(s))
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

X = int(stdin.readline())
if X == 0:
    print(1)
else:
    print(0)
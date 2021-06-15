# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = list(str(stdin.readline().rstrip()))

a, b, c = S.count("t"), S.count("r"), S.count("e")
print(min(a, b, c // 2))
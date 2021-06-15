# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = str(stdin.readline().rstrip())

if "575" in S:
    print("YES")
else:
    print("NO")
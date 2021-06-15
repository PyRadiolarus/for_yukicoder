# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = [stdin.readline().rstrip() for i in range(3)]
c = S.count("RED")
if c < 2:
    print("BLUE")
else:
    print("RED")
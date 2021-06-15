# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = str(stdin.readline().rstrip())
l = S.find("XXX")
w = S.find("OOO")
if l == w == -1:
    print("NA")
elif (w == -1 and l >= 0) or (l != -1 and w != -1 and l < w):
    print("West")
else:
    print("East")
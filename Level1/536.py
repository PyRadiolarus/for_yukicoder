# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = str(stdin.readline().rstrip())
c = S.find("ai",-2)
if c != -1:
    print(S[:-2] + "AI")
else:
    print(S + "-AI")
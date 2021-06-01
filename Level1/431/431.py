# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

D_1, D_2, D_3, S = map(int, stdin.readline().split())

if S == 1 or (D_1 + D_2 + D_3) < 2:
    print("SURVIVED")
else:
    print("DEAD")
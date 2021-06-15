# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N, P = map(int, stdin.readline().split())

if P == N * P:
    print("=")
else:
    print("!=")
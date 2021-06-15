# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

S, F = map(int, stdin.readline().split())
res = S // F + 1
print(res)
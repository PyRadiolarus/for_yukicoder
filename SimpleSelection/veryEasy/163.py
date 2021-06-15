# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

s = stdin.readline().rstrip()
print(s.swapcase())
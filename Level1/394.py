# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = [int(i) for i in stdin.readline().split()]
S.sort()
S = S[1:-1]
print("{:.2f}".format(sum(S) / 4))
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

from math import ceil
X = int(stdin.readline())
Y = int(stdin.readline())
L = int(stdin.readline())

count = 0

if Y >= 0 and X == 0:
    count = ceil(Y / L)
elif Y >= 0 and abs(X) > 0:
    count = ceil(Y / L) + 1 + ceil(abs(X) / L)
else:
    count = ceil(abs(X) / L) + ceil(abs(Y) / L) + 2

print(count)
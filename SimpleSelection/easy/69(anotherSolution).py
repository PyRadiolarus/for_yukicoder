# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

import itertools
A = str(stdin.readline().rstrip())
B = str(stdin.readline().rstrip())

anagramable = ["".join(v) for v in itertools.permutations(A)]

if B in anagramable:
    print("YES")
else:
    print("NO")
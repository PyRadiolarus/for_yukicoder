# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

H, N = map(int, stdin.readline().split())
T = [stdin.readline().rstrip() for i in range(N-1)]
T = [int(i) for i in T]
T.append(H)
T.sort(reverse=True)
c = T.index(H) + 1
if c % 10 == 1:
    print(str(c) + "st")
elif c % 10 == 2:
    print(str(c) + "nd")
elif c % 10 == 3:
    print(str(c) + "rd")
else:
    print(str(c) + "th")
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

import collections
N = int(stdin.readline())
A = [stdin.readline().split() for i in range(N)]
A = sum(A, [])
A = [int(i) for i in A]

C = collections.Counter(A)
item = list(C.items())

res, remains = 0, 0

for i in range(len(item)):
    num = item[i][0]
    count = item[i][1]
    q, mod = divmod(count, 2)
    res += q
    remains += mod

res += remains // 4
print(res)
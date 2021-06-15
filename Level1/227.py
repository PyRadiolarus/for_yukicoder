# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

import collections
A = list(stdin.readline().split())
A = [int(i) for i in A]
b = set(A)
C = collections.Counter(A)
v, c = zip(*C.most_common(1))
v, c_2 = zip(*C.most_common(2))
c = sum(c)
c_2 = sum(c_2)
if c == 2:
    if c_2 == 4:
        print("TWO PAIR")
    else:
        print("ONE PAIR")
elif c == 3:
    if c_2 == 4:
        print("THREE CARD")
    else:
        print("FULL HOUSE")
else:
    print("NO HAND")
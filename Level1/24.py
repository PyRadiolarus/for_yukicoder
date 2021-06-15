# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline())
sl = []
o_num = 100
sample = set(range(10))
for v in range(N):
    l = list(stdin.readline().split())
    nl = [int(i) for i in l[0:4]]
    num = set(nl)
    if l[4] == "NO":
        sample = sample - num
    else:
        if o_num == 100:
            o_num = sample
        sample = o_num & num
        o_num = num
    if len(sample) == 1:
        break
sample = list(sample)
print(sample[0])
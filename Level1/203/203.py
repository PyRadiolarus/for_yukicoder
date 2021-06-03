# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

w1 = [i for i in stdin.readline().rstrip()]
w2 = [i for i in stdin.readline().rstrip()]
l = w1 + w2

count = 0
res = 0

for i in range(len(l)):
    test = l[i]
    if test == "o":
        count += 1
        res = max(count, res)
    else:
        count = 0

print(res)
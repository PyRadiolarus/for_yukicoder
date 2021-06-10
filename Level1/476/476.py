# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

n, a = map(int, stdin.readline().split())
x = [int(i) for i in stdin.readline().split()]
r_a = sum(x) / n

if a == r_a:
    print("YES")
else:
    print("NO")
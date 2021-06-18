# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
res = 0
for i in range(N):
    s, f = map(str,stdin.readline().split())
    s_h, s_m = s.split(":")
    f_h, f_m = f.split(":")
    s_h, s_m, f_h, f_m = int(s_h), int(s_m), int(f_h), int(f_m)
    s = s_h * 60 + s_m
    f = f_h * 60 + f_m
    res += ((f - s) + 1440) % 1440
print(res)
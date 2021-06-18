# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

h, m = stdin.readline().split(":")
h, m = int(h), int(m)
m += 5
if m > 59:
    h += 1
    m -= 60
if h > 23:
    h -= 24
h, m = str(h), str(m)

print(h.zfill(2) + ":" + m.zfill(2))
# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = list(str(stdin.readline().rstrip()))
decodel = []
for v in range(1,len(S)+1):
    ord_v = ord(S[v-1]) - (65 + v)
    while ord_v < 0:
        ord_v += 26
    ord_v = ord_v + 65
    res = chr(ord_v)
    decodel.append(res)
decode = "".join(decodel)
print(decode)
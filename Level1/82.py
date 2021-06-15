# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

W, H, B = stdin.readline().split()
W, H  = int(W), int(H)
c1 = B
if B == "B":
    c2 = "W"
else:
    c2 = "B"
for i in range(H):
    sq_out = ""
    for j in range(W):
        if j % 2 == 0:
            sq_out += c1
        else:
            sq_out += c2
    c2, c1 = c1, c2
    print(sq_out)
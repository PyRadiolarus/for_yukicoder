# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

S = [i for i in stdin.readline().rstrip()]
x, y = 0, 0
for i in S:
    if i == "N":
        y += 1
    elif i == "E":
        x += 1
    elif i == "W":
        x -= 1
    else:
        y -= 1
print(((x**2)+(y**2))**0.5)
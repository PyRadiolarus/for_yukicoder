# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

B = [int(i) for i in stdin.readline().split()]

for i in range(1,11):
    if i in B:
        pass
    else:
        print(i)
        break
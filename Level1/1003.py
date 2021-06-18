# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())

if N % 6:
    print("No")
else:
    print("Yes")
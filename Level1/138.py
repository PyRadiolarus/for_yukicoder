# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

A = [int(i) for i in stdin.readline().split(".")]
B = [int(i) for i in stdin.readline().split(".")]

if A[0] < B[0]:
    print("NO")
elif A[0] == B[0]:
    if A[1] < B[1]:
        print("NO")
    elif A[1] == B[1] and A[2] < B[2]:
        print("NO")
    else:
        print("YES")
else:
    print("YES")
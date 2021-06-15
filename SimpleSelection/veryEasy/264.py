# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N, K = map(int, stdin.readline().split())

if N == K:
    print("Drew")
else:
    if N == 0:
        if K == 1:
            print("Won")
        else:
            print("Lost")
    elif N == 1:
        if K == 0:
            print("Lost")
        else:
            print("Won")
    else:
        if K == 0:
            print("Won")
        else:
            print("Lost")
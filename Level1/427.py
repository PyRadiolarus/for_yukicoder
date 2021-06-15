# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

H, W = map(int, stdin.readline().split())

if W == H * 0.75:
    print("TATE")
else:
    print("YOKO")
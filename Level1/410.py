# -*- coding: utf-8 -*-
# 最短経路問題なのでマンハッタン距離を用いる。出会う場所は最短距離の半分。
from sys import stdin
stdin = open("../stdin.txt")

Px, Py = map(int, stdin.readline().split())
Qx, Qy = map(int, stdin.readline().split())

print((abs(Px - Qx) + abs(Py - Qy)) / 2)
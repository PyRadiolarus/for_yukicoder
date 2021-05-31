# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

D, P = map(int, stdin.readline().split())
price = D + D * (P / 100)
print(int(price))
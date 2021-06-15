# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

from math import floor
K = int(stdin.readline())
S = int(stdin.readline())
print(floor(S / ((100 - K) / 100)))
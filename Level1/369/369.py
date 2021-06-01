# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
v = int(stdin.readline())

print(sum(A)-v)
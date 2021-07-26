from sys import stdin
stdin = open("../stdin.txt")

A, B = (int(i) for i in stdin.readline().split())
if A == B: print(min(A, B) * 2 - 1)
else: print(min(A, B) * 2)
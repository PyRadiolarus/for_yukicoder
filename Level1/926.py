from sys import stdin
stdin = open("../stdin.txt")

A, B, C = (int(i) for i in stdin.readline().split())
print(A/B*C)
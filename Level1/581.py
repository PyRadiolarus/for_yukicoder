from sys import stdin
stdin = open("../stdin.txt")

A, C = map(int, stdin.readline().split())
print(A^C)
from sys import stdin
stdin = open("../stdin.txt")

X, N, M = (int(i) for i in stdin.readline().split())
A = [int(j) for j in stdin.readline().split()]
B = [int(k) for k in stdin.readline().split()]
mr = A.count(X)
va = B.count(X)
if va == mr == 1: print("MrMaxValu")
elif mr == 1: print("MrMax")
elif va == 1: print("MaxValu")
else: print(-1)
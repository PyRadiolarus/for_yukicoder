from os import sep
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
maxd = A[N-1] - A[0]
mind = maxd
for i in range(N-1):
    checkd = A[i+1] - A[i]
    mind = min(mind, checkd)
print(mind,maxd,sep="\n")
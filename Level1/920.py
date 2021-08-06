from sys import stdin
stdin = open("../stdin.txt")

X, Y, Z = (int(i) for i in stdin.readline().split())
a = min(X, Y)
a += min(Z, (abs(X - Y) + Z) // 2)
print(a)
from sys import stdin
stdin = open("../stdin.txt")

X, Y, Z = (int(i) for i in stdin.readline().split())
if X > Z: print(Z)
elif Y > Z: print(Z - 1)
else: print(Z - 2)
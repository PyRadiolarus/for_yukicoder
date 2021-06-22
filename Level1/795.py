from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
M = int(stdin.readline())

if N*10 == M:
    print("Yes")
else:
    print("No")
from sys import stdin
stdin = open("../stdin.txt")

N, M = map(int, stdin.readline().split())
print("".join([stdin.readline().rstrip() for i in range(N)]).count("W"))
from sys import stdin
stdin = open("../stdin.txt")

N, K = map(int, stdin.readline().split())
n = 2 ** N // 2 ** K
print(n)
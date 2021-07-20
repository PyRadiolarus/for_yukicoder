from sys import stdin
stdin = open("../stdin.txt")

A, B = map(int, stdin.readline().split())
if A + 1 <= B : S = "YES"
else : S = "NO"
print(S, abs(A + 1 - B), sep="\n")
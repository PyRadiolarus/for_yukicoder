from sys import stdin
stdin = open("../stdin.txt")

S = [i for i in stdin.readline().rstrip()]
i, j = map(int, stdin.readline().split())
S[i], S[j] = S[j], S[i]
S = "".join(S)
print(S)
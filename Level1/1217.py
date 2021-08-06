from sys import stdin
stdin = open("../stdin.txt")

C = "abcdefghijklmnopqrstuvwxyz"
S = stdin.readline().rstrip()

for i in range(len(S)):
    char = S[i]
    if char != C[i]:print(C[i] + "to" + char)
    else:pass
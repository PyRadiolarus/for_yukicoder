from sys import stdin
stdin = open("../stdin.txt")

S = stdin.readline().rstrip()
n, m = divmod(len(S),2)
if m == 0 and S[:n] == S[n:]:print("YES")
else:print("NO")
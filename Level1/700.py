from sys import stdin
stdin = open("../stdin.txt")

n, m = map(int, stdin.readline().split())
res = 0
for i in range(n):
    s = stdin.readline().rstrip()
    if s.count("LOVE") != 0:
        res += 1
        break
    else:
        pass
if res != 0:
    print("YES")
else:
    print("NO")
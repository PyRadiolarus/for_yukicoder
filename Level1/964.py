from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
if N == 1:
    print(1)
else:
    out = str()
    for i in range(N-1,-1,-1):
        s = str(i) * N
        out += s
    print(out)
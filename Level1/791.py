from sys import stdin
stdin = open("../stdin.txt")

N = stdin.readline().rstrip()
res = 0
if N[0] != "1":
    res = -1
else:
    N = N[1:]
    numl = {i for i in N}
    numl = {int(i) for i in numl}
    if len(numl) == 1 and 3 in numl:
        res = len(N)
    else:
        res = -1
print(res)
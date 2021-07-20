from sys import stdin
stdin = open("../stdin.txt")

T = int(stdin.readline())
X = [stdin.readline().rstrip() for i in range(T)]
X = [int(i) for i in X]
res = 0
for i in range(T):
    if i == 0:
        diff = abs(0 - X[i])
    else:
        diff = abs(X[i] - X[i-1])
    if diff == 1:
        pass
    else:
        res = -1
        break
if res != 0:
    print("F")
else:
    print("T")
from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
res = 0
for i in range(100):
    if i == 0:res = sum(list(map(int, str(N))))
    else:res = sum(list(map(int, str(res))))
    if res - 10 < 0:break
print(res)
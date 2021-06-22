from sys import stdin
stdin = open("../stdin.txt")

A = [int(i) for i in stdin.readline().split()]
res = 0
for i in A:
    if i % 3 == 0 and i % 5 == 0:res += 8
    elif i % 3 == 0 or i % 5 == 0:res += 4
    else:res += len(str(i))
print(res)
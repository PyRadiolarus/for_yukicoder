from sys import stdin
stdin = open("../stdin.txt")

n = [int(i) for i in stdin.readline().split()]
n.sort()
if n == list(range(n[0], n[3] + 1)):
    print("Yes")
else:
    print("No")
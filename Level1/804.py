from sys import stdin
stdin = open("../stdin.txt")

n = [int(i) for i in stdin.readline().split()]
print(min(n[0], n[1] // n[2], n[3] // (n[2] + 1)))
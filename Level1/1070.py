from sys import stdin
stdin = open("../stdin.txt")

C = stdin.readline().rstrip()
count = C.count("0")
print(len(C) - count - 1)
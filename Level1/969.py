from sys import stdin
stdin = open("../stdin.txt")

X = int(stdin.readline())
if X == 0 or X == 4 or X == 10: print("Yes")
else: print("No")
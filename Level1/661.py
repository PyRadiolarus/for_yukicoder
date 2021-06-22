from sys import stdin
stdin = open("../stdin.txt")

n = int(stdin.readline())
for i in range(n):
    a = int(stdin.readline())
    if a % 8 == 0 and a % 10 == 0:
        print("ikisugi")
    elif a % 8 == 0:
        print("iki")
    elif a % 10 == 0:
        print("sugi")
    else:
        print(a//3)
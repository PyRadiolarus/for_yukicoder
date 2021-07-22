from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
q, a = divmod(N % 180, 90)
if q > 0 and a == 0: print("Yes")
else: print("No")
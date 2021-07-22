from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
m = N % 6
if m == 1:
    print(2)
elif m == 2:
    print(8)
elif m == 3:
    print(5)
elif m == 4:
    print(7)
elif m == 5:
    print(1)
elif m == 0:
    print(4)
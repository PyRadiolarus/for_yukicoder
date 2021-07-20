from sys import stdin
stdin = open("../stdin.txt")

P_yuki = int(stdin.readline())
P_chag = int(stdin.readline())
N = int(stdin.readline())
R = [stdin.readline().rstrip() for i in range(N)]
R = [int(i) for i in R]
diff = len(R) - len(set(R))
if diff == 0:
    print(0)
else:
    print(diff * (P_yuki + P_chag))
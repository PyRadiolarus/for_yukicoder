from sys import stdin
stdin = open("../stdin.txt")

# 解法その1
#import math
#N = int(stdin.readline()) - 7
#b = 10**9
#if N > b:
#    N, b = b, N
#print(int(math.log10(b // N)))

# 解法その2
print(abs(len(stdin.readline().rstrip()) - 10))
# 関数を使わないバージョン。コード長455Byte、実行時間21ms、使用メモリ7944KB。コンパイル時間は64ms。
from sys import stdin
stdin = open("../stdin.txt")

N, M = (int(i) for i in stdin.readline().split())
opB = [i for i in stdin.readline().split()]
B = [int(i) for i in opB[1:]]
A = [stdin.readline().rstrip() for i in range(N)]
A = [int(i) for i in A]

if opB[0] == "+":
    for i in A:
        l = []
        for j in B:
            num = i + j
            l.append(num)
        print(" ".join(map(str,l)))
else:
    for i in A:
        l = []
        for j in B:
            num = i * j
            l.append(num)
        print(" ".join(map(str,l)))
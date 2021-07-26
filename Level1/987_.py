# 関数を使うバージョン。コード長429Byte、実行時間20ms、使用メモリ7908KB。コンパイル時間は68ms。
from sys import stdin
stdin = open("../stdin.txt")

def matrixSolve(op, A, B):
    for i in A:
        l = []
        for j in B:
            if op == "+":
                num = i + j
            else:
                num = i * j
            l.append(num)
        print(" ".join(map(str, l)))

N, M = (int(i) for i in stdin.readline().split())
opB = [i for i in stdin.readline().split()]
B = [int(i) for i in opB[1:]]
A = [stdin.readline().rstrip() for i in range(N)]
A = [int(i) for i in A]
op = opB[0]
matrixSolve(op, A, B)
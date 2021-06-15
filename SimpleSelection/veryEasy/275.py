# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../../stdin.txt")

N = int(stdin.readline())
A = [int(i) for i in stdin.readline().split()]
A.sort()
if len(A) % 2 == 1:
    m_index = len(A) // 2
    print(A[m_index])
else:
    mNum_1 = A[len(A) // 2 - 1]
    mNum_2 = A[len(A) // 2]
    med = (mNum_1 + mNum_2) / 2
    print(round(med, 1))
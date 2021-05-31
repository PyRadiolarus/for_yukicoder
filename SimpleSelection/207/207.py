# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("stdin.txt")

A, B = map(int, stdin.readline().split())
sample = list(range(A,B+1))

def gen(n):
    if n < 10:
        yield n
    else:
        for j in gen(n/10):
            yield j
        yield n%10

for i in range(len(sample)):
    testNum = sample[i]
    if testNum % 3 == 0 or testNum % 10 == 3:
        print(testNum)
    else:
        testl = [int(k) for k in gen(testNum)]
        if 3 in testl:
            print(testNum)
        else:
            pass
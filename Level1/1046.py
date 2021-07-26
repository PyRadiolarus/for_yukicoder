from sys import stdin
stdin = open("../stdin.txt")

N, K = (int(i) for i in stdin.readline().split())
A = [int(i) for i in stdin.readline().split()]
A.sort(reverse=True)
A_ = A[:K]
S = [i for i in A_ if i > 0]
if len(S) == 0:
    print(A_[0])
else:
    print(sum(S))
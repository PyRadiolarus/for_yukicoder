from sys import stdin
stdin = open("../stdin.txt")

S = [int(i) for i in stdin.readline().rstrip()]
score = 0

for i in S:
    if i != 0:
        score += i
    else:
        score += 10
print(score)
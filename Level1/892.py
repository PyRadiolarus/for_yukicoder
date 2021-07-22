from sys import stdin
stdin = open("../stdin.txt")

A_1, B_1, A_2, B_2, A_3, B_3 = (int(i) for i in stdin.readline().split())
count = 0
if A_1 % 2 == 0: count += 1
else: count += 10
if A_2 % 2 == 0: count += 1
else: count += 10
if A_3 % 2 == 0: count += 1
else: count += 10
if count == 3 or count == 21: print(":-)")
else: print(":-(")
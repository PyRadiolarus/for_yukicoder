from sys import stdin
stdin = open("../stdin.txt")

q, m = divmod(int(stdin.readline()),2)
print(q+m)
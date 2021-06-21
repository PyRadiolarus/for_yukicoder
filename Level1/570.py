from sys import stdin
stdin = open("../stdin.txt")

H = [stdin.readline().rstrip() for i in range(3)]
N = ["A", "B", "C"]
d = dict(zip(H,N))
d = sorted(d.items(), key= lambda x:x[0], reverse= True)
for i in d:
    print(i[1])
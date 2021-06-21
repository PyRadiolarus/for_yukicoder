from sys import stdin
stdin = open("../stdin.txt")

N = int(stdin.readline())
x = [int(i) for i in stdin.readline().split()]
x.sort()
res = x[1] - x[0]
if len(x) == len(set(x)):
    for i in range(2,len(x)):
        a = x[i] - x[i-1]
        if a != res:
            res = -1
            break
        else:
            pass
    if res == -1:
        print("NO")
    else:
        print("YES")

else:
    print("NO")
from sys import stdin
stdin = open("../stdin.txt")

import re
S = stdin.readline().rstrip()
out = int()
for i in range(len(S)):
    checkStr = S[i]
    if i % 2 == 0:
        if checkStr.islower():
            pass
        else:
            out -= 1
            break
    else:
        c = re.fullmatch("\s", checkStr)
        if c == None:
            out -= 1
            break
        else:
            pass
if out == -1:
    print("No")
else:
    print("Yes")
from sys import stdin
stdin = open("../stdin.txt")

import re
S = stdin.readline().rstrip()
S_ = [m.span() for m in re.finditer("ao",S)]
if len(S_) == 0:
    print(S) 
else:
    for i in range(len(S_)):
        s, e = S_[i]
        S = S[0:s]+"ki"+S[e:]
    print(S)
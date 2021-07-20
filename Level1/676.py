from sys import stdin
stdin = open("../stdin.txt")

S = [str(i) for i in stdin.readline().rstrip()]
out = []
for i in S:
    if i == "I" or i == "l" : i = "1"
    elif i == "O" or i == "o" : i = "0"
    else : pass
    out.append(i)
out = "".join(out)
print(out)
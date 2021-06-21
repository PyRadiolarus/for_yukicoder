from sys import stdin
stdin = open("../stdin.txt")

S1, T = stdin.readline().split()
T = int(T)
if S1 == "IX":
    S1 = "VIIII"
S1 = (S1.count("I") + (S1.count("V") * 5) + (S1.count("X") * 10))
S2 = (S1 + T) % 12
out = []
if S2 - 10 >= 0:
    out += "X"
    S2 -= 10
if S2 - 5 >= 0:
    out += "V"
    S2 -= 5
while 1 <= S2 < 5:
    out += "I"
    S2 -= 1
out = "".join(out)
if out == "VIIII":
    out = "IX"
elif out == "":
    out = "XII"
print(out)
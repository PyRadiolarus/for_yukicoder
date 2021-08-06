from sys import stdin
stdin = open("../stdin.txt")

S1, S2 = map(str, stdin.readline().rstrip().split())
if S1 == "Sat" or S1 == "Sun":
    if S2 == "Sat" or S2 == "Sun":
        print("8/33")
    else:
        print("8/32")
else:
    print("8/31")
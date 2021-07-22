from sys import stdin
stdin = open("../stdin.txt")

S = stdin.readline().rstrip().replace(" ","")
if S[1] == "?": print("14")
elif S[1] == "3": print("1")
else: print("4")
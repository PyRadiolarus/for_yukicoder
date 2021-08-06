from sys import stdin
stdin = open("../stdin.txt")

S = [i for i in stdin.readline().rstrip().split(",")]
if len(set(S)) == 1 and "AC" in S: print("Done!")
else: print("Failed...")
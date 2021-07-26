from sys import stdin
stdin = open("../stdin.txt")

# オリジナルコード
print("{:,}".format(int(stdin.readline())))
# 提出ACコード最小長
print(f"{int(stdin.readline()):,}")
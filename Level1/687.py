from sys import stdin
stdin = open("../stdin.txt")

import math
n = int(stdin.readline()) / 2
print(math.floor(n),math.ceil(n))
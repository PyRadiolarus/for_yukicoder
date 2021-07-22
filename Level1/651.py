from sys import stdin
stdin = open("../stdin.txt")

a = int(stdin.readline())
time = 600
time += a / 100 * 60
h, m = divmod(time, 60)
h, m = str(int(h)), str(int(m))
if int(m) < 10:
    m = m.zfill(2)
print(h + ":" + m)
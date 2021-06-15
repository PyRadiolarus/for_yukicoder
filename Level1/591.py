# -*- coding: utf-8 -*-
from sys import stdin
stdin = open("../stdin.txt")

eye = str(stdin.readline().rstrip())
mouth = str(stdin.readline().rstrip())

print("(" + eye + mouth + eye + ")/")
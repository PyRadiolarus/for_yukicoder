# -*- coding: utf-8 -*-
monthl = list(range(1,13))
datel_1 = list(range(1,29))
datel_2 = list(range(1,31))
datel_3 = list(range(1,32))

res = 0

for i in monthl:
    if i == 2:
        for j in datel_1:
            q, mod = divmod(j,10)
            if i == q + mod:
                res += 1
    elif i == 4 or i == 6 or i == 9 or i == 11:
        for j in datel_2:
            q, mod = divmod(j,10)
            if i == q + mod:
                res += 1
    else:
        for j in datel_3:
            q, mod = divmod(j,10)
            if i == q + mod:
                res += 1

print(res)
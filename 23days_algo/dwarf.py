#https://www.acmicpc.net/problem/2309
dwafs = []
for i in range(9):
    dwafs.append(int(input()))
find = sum(dwafs) - 100
tall = 0
isFind = False
for idx, i in enumerate(dwafs):
    tall = i
    for a in dwafs:
        if i == a:
            continue
        if tall + a == 40:
            del dwafs[idx]
            isFind = True
    if isFind:
        del dwafs[idx]
        break

a = sorted(dwafs)
res = ""
for c in a:
    res += str(c) +"\n"
print(res)

"""
20
7
23
19
10
15
25
8
13
"""
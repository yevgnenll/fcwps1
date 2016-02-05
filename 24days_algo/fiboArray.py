start = int(input()) % 1000000
print(start)
res = [0,1]
cur =2
while len(res) <= start:
    if start == 0:
        print(0)
        break
    if start == 1:
        print(1)
        break

    f2 = res[cur-2]
    f1 = res[cur-1]
    res.append(f2+f1)
    cur += 1
print(res[start], len(res))
#1000000000000000000
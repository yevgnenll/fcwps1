#https://www.acmicpc.net/problem/2748
start = int(input())
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
print(res[-1])

def findpibo(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    return findpibo(n-1)+findpibo(n-2)



# #https://www.acmicpc.net/problem/2526
n,p = map(int, input().split())
# 67, 31
check = list()
first = n
cnt =0
while True:
    res = (first * n) % p
    if res in check:
        check.append(res)

        for idx, a in enumerate(check):
            if a == res:
                cnt = idx+1
                break

        break
    check.append(res)
    first = res
print(len(check[cnt:]))

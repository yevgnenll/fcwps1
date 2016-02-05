import sys
sys.setrecursionlimit(10000)
v, e = map(int, input().split())
a= [[] for _ in range(v+1)]
cnt = 0
for _ in range(e):
    i, j = map(int, input().split())
    a[i].append(j)
    a[j].append(i)
for i in a:
    i.sort()

check = [False for _ in range(v+1)]
def dfs(a, check, n , now):
    #n은 정점의 갯수
    if check[now]:
        return
    check[now] = True
    for i in a[now]:
        dfs(a, check, n, i)

for idx, ch in enumerate(check):
    if idx == 0:
        continue
    if not ch:
        dfs(a, check, v, idx)
        cnt += 1
print(cnt)
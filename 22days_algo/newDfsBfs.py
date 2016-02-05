#https://www.acmicpc.net/problem/1260
n, m, start = map(int, input().split())
# 어디를 방문했는지 체크하는 변수
check = [False for _ in range(n+1)]
a = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1, n+1):
    a[i].sort()
print(a)
def dfs(a, check, n , now):
    if check[now]:
        return
    check[now] = True
    print(now, end=' ')
    for i in a[now]:
        dfs(a, check, n, i)
dfs(a, check, n, start)
print()
check = [False for _ in range(n+1)]
def bfs(a, check, n, now):
    que = [start] # que형태 일단 처음은 start가 들어간다
    check[start] = True #들어간 곳을 체크한다
    while que: # que는 계속 빠져나간다
        now = que[0] # 지금위치는 que에서 제일 처음
        que = que[1:]
        print(now, end=' ')
        for i in a[now]:
            if not check[i]:
                que.append(i)
                check[i] = True
bfs(a, check, n, start)
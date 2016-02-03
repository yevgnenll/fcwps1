
#n 정점 m간선 s 시작
# 맨처음 입력받는 3개
# n: vertax갯수, m:간선 갯수, 시작지점
n,m,s = map(int, input().split())
a = [[] for i in range(n+1)]
# a = [False for i in range(n+1)]

# 어디서 어디로 이어지는지 양방향으로 접근하기 때문에 동시에 append함
for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
    #a[u][v]=a[v][u]= True

dfs_stack = list()
bfs_stack = list()
que = list()
dfs_stack.append(s)
while True:
    for po in a[s]:
        if po not in dfs_stack:
            dfs_stack.append(po)
            s = po
            break
        else:
            continue
    if len(dfs_stack) == n:
        break
# bfs_stack.append(s)
# que.append(s)
# while True:
#     print(bfs_stack, que)
#     for po in a[s]:
#         if po not in que:
#             bfs_stack.append(po)
#
#     mid = bfs_stack.pop(0)
#     que.append(mid)
#     s = mid
#     if len(que) == n:
#         break
#
# print(dfs_stack)


##---- 인접행렬

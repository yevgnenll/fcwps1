# mem, cnt = map(int, input().split())
# # mem = 7
# # cnt = 3
# que = list()
# res = "<"
# cur = 1
# for i in range(1, mem+1):
#     que.append(i)
# # print(que)
# while len(que) > 1:
#     for num in que:
#         if cur % cnt == 0:
#             res += str(que[0])+", "
#             del que[0]
#         else :
#             ft = int(que[0])
#             del que[0]
#             que.append(ft)
#         cur += 1
#     # print(que)
#
# res += str(que[0])
# res += ">"
# print(res)
#
#<3, 6, 2, 7, 5, 1, 4>

# mems, cnt = map(int, input().split())
mem = 7
cnt = 3
que = list()
res = "<"
cur = 1
for i in range(1, mem+1):
    que.append(i)
# print(que)
while len(que) > 1:
    for num in que:
        if cur % cnt == 0:
            res += str(que.pop())+", "
        else :
            que.append(que.pop())
        cur += 1
    # print(que)

res += str(que[0])
res += ">"
print(res)
#<3, 6, 2, 7, 5, 1, 4>

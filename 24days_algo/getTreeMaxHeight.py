#https://www.acmicpc.net/problem/2805
cnt, limit = map(int, input().split())
trees = list(map(int, input().split()))

def checkTree(height):
    # 자르는 높히가 적당한지 체크함
    getHeight = 0
    for tree in trees:
        if tree > height:
            getHeight += (tree - height)
    # 제한보다 높을때 -> 칼의 높이를 높혀야 한다
    if getHeight >= limit:
        return True
    else:
        #제한보다 낮을때 -> 칼의 높이를 낮춰야 한다
        return False
# 가장 높은 범위
up = max(trees)
# 가장 낮은 범위
earth = 0
#그래서 칼의 높이
knife_height = 0

# up과 earth의 극한은 knife_height에 수렴한다
while earth <= up:
    #최초 높이 지정
    mid = (up+earth) // 2
    #현재 높이가 더 높다면
    if checkTree(mid):
        # 칼의 높이가 가장 높은경우 선택(획득한 나무의 길이가 limit에 가장 근접한 범위)
        knife_height = max(mid, knife_height)
        earth = mid +1
    else:
        up = mid - 1
print(knife_height)


#---------------동현이 yield 설명---------------
# def make_gen(num, last = 10, step= 1):
#     number = num
#     while number < last:
#         yield number
#         number += step
#
# ranger = make_gen(1, 3)
#
#
# for x in ranger:
#     print(x)
#
# def make_gen_list(num, last = 10, step= 1):
#     number = num
#     res = list()
#     while number < last:
#         res.append(number)
#         number += step
#     return res
#
# ranger = make_gen(1, 3)
# print(type(ranger))
# for x in ranger:
#     print(x)
# print(ranger)




"""
4 7
20 15 10 17
"""
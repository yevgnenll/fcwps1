#https://www.acmicpc.net/problem/1978
import math
#
# num = int(input())
# cnt = 0
#
# n = list(map(int, input().split()))
# # 1, 3, 5, 7
#
# def find(key):
#
#     if key < 2:
#         return False
#     else :
#         for i in range(2, key):
#             if i * i <= key:
#                 if key % i == 0:
#                     return False
#             else :
#                 break
#         return True
#
#
# cnt = 0
# for a in n:
#     if find(a):
#         cnt += 1
# print(cnt)
#

def isPrime(number):
    """
    number가 소수라면 True 아니면 False
    2~루트 number까지만 모두 나누어보면 된다
    """
    if number < 2:
        return False
    else:
        i = 2
        while True:
            if i * i <= number:
                if number % i == 0:
                    return False
            else:
                return True
            i += 1
#------------------------ 함수 끝
print(isPrime(2))






"""
num = int(input())
cnt = 0

n = list(map(int, input().split()))
# 1, 3, 5, 7

def find(key):

    if key < 2:
        return False
    elif key == 2:
        return True
    else :
        i = 1
        while i * i <= key:
            i+=1
            print(key, i, key% i)
            if key % i == 0:
                return False
            else :
                return True

cnt = 0
for a in n:
    if find(a):
        cnt += 1
print(cnt)
"""
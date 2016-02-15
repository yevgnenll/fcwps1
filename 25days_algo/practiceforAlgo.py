# https://www.acmicpc.net/problem/1008
# a,b = map(int, input().split())
# c = float(a/b)
# print(c)

# https://www.acmicpc.net/problem/1003
# count = int(input())
#
# nums = []
# for num in range(count):
#     nums.append(int(input()))
#
# cnt_one = [0]*41
# cnt_zero = [0]*41
#
# cnt_one[1] = 1
# cnt_zero[0] = 1
#
# for i in range(2, 41):
#     cnt_zero[i] = cnt_zero[i-1]+cnt_zero[i-2]
#     cnt_one[i] = cnt_one[i-1]+cnt_one[i-2]
# for n in nums:
#     print("%d %d"%(cnt_zero[n], cnt_one[n]))

# https://www.acmicpc.net/problem/1026
# cnt = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# a_desc = sorted(a,reverse=True)
# b_asc = sorted(b)
#
# sumNum = 0
# for i in range(cnt):
#     sumNum += (a_desc[i] * b_asc[i])
# print(sumNum)

# https://www.acmicpc.net/problem/9498
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력
# a = int(input())
#
# if a >= 90:
#     print("A")
# elif a >= 80:
#     print("B")
# elif a >= 70:
#     print("C")
# elif a >= 60:
#     print("D")
# else:
#     print("F")

# https://www.acmicpc.net/problem/10869
# a,b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# https://www.acmicpc.net/problem/2475
# nums = list(map(int, input().split()))
# allNums = 0
# for i in nums:
#     allNums += i**2
# print(allNums%10)

# https://www.acmicpc.net/problem/1110
# num = int(input())
# duplicated = num
# cnt = 0
# while True:
#     a = num // 10
#     b = num % 10
#     c = (a+b) % 10
#     num = b*10 + c
#     cnt += 1
#     if duplicated == num:
#         break
# print(cnt)

num = int(input())
print((num*(1+num))/2)
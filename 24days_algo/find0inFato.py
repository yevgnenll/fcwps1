#https://www.acmicpc.net/problem/1676
# 주어진 숫자 n의 팩토리얼 n!에서 0의 갯수를 찾는다
# 0 <= n <= 500

facto = int(input())
res = (facto//5)+ (facto//25)+(facto//125)
print(res)
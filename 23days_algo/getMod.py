#https://www.acmicpc.net/problem/10430
"""
(A+B)%C는 (A%C + B%C)%C 와 같을까?
(A×B)%C는 (A%C × B%C)%C 와 같을까?
세 수 A, B, C가 주어졌을 때, 위의 네가지 값을 구하는 프로그램을 작성하시오.
"""
a, b, c = map(int, input().split())
first=(a+b)%c
second =(a%c + b%c) % c
third = (a*b)%c
forth = (a%c * b%c)%c
print(first)
print(second)
print(third)
print(forth)
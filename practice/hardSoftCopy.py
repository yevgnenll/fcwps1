#-*- encoding:utf-8 -*-

"""
hardcopy, softcopy에 대한 개념 이해와 학습
학습목표 자료구조 graph를 할때 경험했던 오류가 만들어진 n*n 리스트가 소프트카피인게 원인이었음
linked list를 구현할때도 소프트카피 하드카피에 대한 개념의 확립이 안되어있음을 확인함
"""

a = 1
b= [2,3,4]
print("a의 주소 ",id(a),"b의 주소" ,id(b))
c = a
print("c = a 대입")
print("c의 값:",c,"c의 주소:", id(c),"a의 주소:", id(a), "b의 주소" ,id(b))
print("c, a의 주소가 일치?", id(c)==id(a))

c = 3
print(c , a)


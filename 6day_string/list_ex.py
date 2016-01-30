# -*- encoding:utf-8 -*-
empty = list()
print (empty)
print(list("abcdef"))
doc = "Returns an iterator of tuples, where the i-th tuple contains the i-th " \
      "element from each of the argument sequences or iterables. The iterator stops " \
      "when the shortest input iterable is exhausted. With a single iterable argument, " \
      "it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. Equivalent to:"
empty = doc.split()
print (empty)
print(len(empty))
print(empty[-2:])

a = "This is my list string"
b = a.split()
b.insert(3, "cute") #연산 결과가 아님
print(b)
#del b[3]
#b.remove("cute")
b.pop(4)
print(b)
c = b
print ("is" in b) #유, 무만 알려준다 이고 아이고 그래서 이게 좋구나
#b.sort() #값을 정렬한다
print(sorted(b)) #로그에서 바로 리턴이 가능함.


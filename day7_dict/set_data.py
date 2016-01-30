drink = {
    "martini": {'vodka', 'vermouth'},
    "black russian": {'vodka', 'kahlua'},
    "white russain":{'cream','kahlua', 'vodka'},
    "manhattan": {'rye', 'vermouth', 'bitters'},
    "screwdriver": {'orange juice', 'vodka'}
}
"""
문자열 처리를 하는데 할당을 하지 않았기 때문에 주석처리처럼 사용한다
print(drink)
print(drink.items())
"""



def isVodka(bev):
    ref = []
    for name, contents in bev.items():
        # a,b = (1,2) 의 개념이다
        #이걸로 name, contents에 각각 key, value가 들어가기 때문에 비교가 가능함
        if 'vodka' in contents:
            ref.append(name)

    return ref

#print(isVodka(drink))

first = {"a", "b", "c", "d", "e", "f"}
second = {"c", "d", "e","g","h"}
third = {"a", "b", "c"}
print("교집합",first.intersection(second)) # intersection은 교집합을 말함

print("합집합", first.union(second))

print("차집합", first.difference(second))
print("반대 - 차집합", second.difference(first))
#set에서 순서는 없다

print("대칭차집합", first.symmetric_difference(second))
print("반대 - 대칭차집합", second.symmetric_difference(first))

print("부분집합", first.issubset(third))
print("부분집합", third.issubset(first))


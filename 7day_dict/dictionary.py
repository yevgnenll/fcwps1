#tol=(['a','b','c'], ['c','d'], ['e','f'])
#print(dict(tol))
"""
los = ['a5','c한','e6']
print(dict(los))

tos = ('ab','cd','ef')
print(dict(tos))

ts= ['한국','미국','중국']
print(dict(ts))
"""


py = {
    'a':'res',
    'b':'aos',
    'c':'jkd'
}

a = py.items()
print(type(a))

print(py)
#할당을 시작함

py['d'] = 'romio'
print(py)
py['d'] = 'jenny'
print(py)


other ={
    'jk':"ruth",
    "la":"list",
    "ti":"1234"
}

print("key  :", other.keys())
print("value:", other.values())
print("k-v  :", other.items())

# print("other: ", other)
#
# py.update(other)
# print(py)
# print(other)
# # 이렇게 병합이 되면 기존의 깊히가 바뀔 수 있다
#
# del other['jk']
# print(other)
# other.clear()
#
# print(other) #clear하면 다 지워짐
#
#
# print('a' in py)
#
# #print(py['marx'])
# print(py.get('marx',"null key"))
# print(py.keys())
#
# list_dic = list(py.keys())
# print(list_dic)
#
# print(py.values())
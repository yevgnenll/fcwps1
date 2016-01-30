a = "월요일", "화요일","수요일"
b= "mon","tue","wed"

c = list(zip(a, b))
d = zip(a,b)
print(c)
print(type(c), type(c[0]))
#print(type(d[0]))
print(d)
print(type(a))

a = list([2**i for i in range(11)])
print(a)

print(0 == 0.0)
print("------", 0 == None) # 이해가 안됨
print(bool(None), bool(0))
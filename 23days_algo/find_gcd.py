#https://www.acmicpc.net/problem/2609
a,b = map(int, input().split())
c = a
d = b
while b >0:
    r = a%b
    a = b
    b = r

l = c*d//a
res = str(a)+" "+str(l)
print(res)
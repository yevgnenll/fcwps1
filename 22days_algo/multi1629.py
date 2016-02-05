#https://www.acmicpc.net/problem/1629
a,b,c = map(int, input().split())
def multiply(a,b,c):
    # if b == 0:
    pass
print(multiply(a,b,c,))

# jeonghyeonlee [12:52 AM]
# n = int(input())
# nlist = list(map(str,input().split()))
# m = int(input())
# a = []
# stack = []
# for _ in range(m):
#    s,e = map(int, input().split())
#    a.append([s,e])
# for i in range(m):
#    b = a[i]
#    if ''.join(nlist[b[0]-1:b[1]]) == ''.join(reversed(nlist[b[0]-1:b[1]])):
#        print(1)
#    else:
#        print(0)
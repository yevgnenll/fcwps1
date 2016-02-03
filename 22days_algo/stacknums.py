cnt = int(input())
a = list()
for _ in range(cnt):
    a.append(int(input()))
# print(a)
# a= [4,3,6,8,7,5,2,1] # 입력받은 값

# cnt = 8
p= [n for n in range(1,cnt+1)]
# p = [1,2,3,4,5,6,7,8]
st = list() #중간 스택
res = list()
mp = a.index(cnt)
# 최대값이 나온 이후로는 반드시 숫자가 예외없이 내림차순이어야 한다
# b, c는 신경쓸 필요 없음
b = a[mp:]
c = sorted(a[mp:],reverse=True)
if b == c:
    while len(a)>0:
        # 일단 처음은 무조건 빼서 중간 스택에 넣는다
        st.append(p.pop(0))
        print("+")
        # print(a, res, p)
        if len(st) == 0:
            break
        # while len(a)>0:
        while len(st)>0:
            # 값을 비교하는 곳
            # 값이 같은지 확인한다
            if st[-1] == a[0]:
                # 값이 같은경우
                mid = st.pop()
                res.append(mid)
                del a[0]
                # print(res,mid)
                print("-")
            else :
                #값이 다른경우
                break
else:
    print("NO")
#
#
# n = int(input())
#
# print(n)
# stack_org = list(range(1,n+1))
# stack_l = list() # input 받는거
# buffer = list() #중간 stack
#
# for _ in range(n):
#    stack_l.append(int(input()))
#
# stack_l = stack_l[::-1]
#
# print(stack_org)
# print(stack_l)
#
#
# while True:
#    buffer.append(stack_org.pop(0))
#    print("+")
#
#    while buffer[-1] == stack_l[-1]:
#        print("-")
#        stack_l.pop()
#        buffer.pop()
#        # print("buffer:",buffer)
#        # print("org_stack:",stack_org)
#        # print("stack_l:",stack_l)
#        if len(buffer) is 0 or len(stack_l) is 0:
#            break
#    if len(stack_org) is 0:
#        if len(buffer) is 0:
#            break
#        else:
#            print("No")
#            break

# cnt = int(input())
cnt = 3
print(cnt)
for i in range(1,cnt+1):
    print(" "*(cnt-i), end="")
    print("*"*i)
for i in range(1, cnt):
    print(" "*i, end="")
    print("*"*(cnt-i))
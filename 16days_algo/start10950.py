cnt = int(input())
for i in range(1, cnt+1):
    print("*"*i, end="")
    print(" "*(-2*i+(2*cnt)), end="")
    print("*"*i)
for i in range(1, cnt):
    print("*"*(-1*i+cnt), end="")
    print(" "*i*2, end="")
    print("*"*(-1*i+cnt))


cnt = int(input())
# print(len("**********"))
# cnt = 5
for i in range(1, cnt):
    print(" "*(i-1), end="")
    print("*"*(-2*i+(2*cnt+1)), end="")
    print()
for i in range(1, cnt+1):
    print(" "*(-1*i+cnt), end="")
    print("*"*(i*2-1), end="")
    print()

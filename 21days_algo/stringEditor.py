#문자열
first = input()
cnt = int(input())
left = list(first)
right = list()
for i in range(cnt):
    keyboard = input().split()
    if keyboard[0] == "L":
        if len(left) == 0:
            continue
        right.append(left.pop())
    elif keyboard[0] == "D":
        if len(right)== 0:
            continue
        left.append(right.pop())
    elif keyboard[0] == "B":
        if len(left) == 0:
            continue
        left.pop()
    elif keyboard[0] == "P":
        left.append(keyboard[1])
    print(left, right)

first = ""
res = left + right[::-1]
for s in res:
    first += s
print(first)
st = input()
# "()(((()())(())()))(())"

stack = list()
fragile = 0
for idx, s in enumerate(st):
    if s == "(":
        stack.append(idx)
    else:
        if idx - stack[-1] > 1 :
            fragile += 1
            stack.pop()
        elif idx - stack[-1] == 1:
            stack.pop()
            fragile += len(stack)

print(fragile)


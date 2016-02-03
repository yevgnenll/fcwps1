num, cnt = map(int, input().split())
cur = 1
check = dict()

check[num] = cur
def splitNum(no, c):
    tem = list(str(no))
    tem2 = list(map(int,tem))
    s = 0
    for a in tem2:
        s += a ** c
    return s

while True:

    all = splitNum(num, cnt)
    if all in check:
        print(check[all]-1)
        break
    else:
        cur += 1
        check[all] = cur
        num = all


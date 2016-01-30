def snail(n):
    """
    정수 n을 집어넣었을때 n*n의 상자가 만들어지고 다음과같이 된다 (n이 5인경우)
     1  2  3  4  5
    16 17 18 19  6
    15 24 25 20  7
    14 23 22 21  8
    13 12 11 10  9
    1. 왼쪽 -> 오른쪽
    2. 위 -> 아래
    3. 오른쪽 -> 왼쪽
    4. 아래 -> 위
    이렇게 4가지의 경우가 존재한다
    :param n:
    :return: 2차원 배열이든 1차원 배열이든 위와같은 값이 나와야 한다.
    """
    arr = [[None for a in range(0,n)] for i in range(0, n)]
    status = ["right", "down", "left", "up"] #4가지 경우
    cnt = 0
    cur = status[cnt%4]
    i, j = 0, 0
    # num = 0
    for loc in range(1, n*n+1):
        # num += 1
        cur =status[cnt%4]
        if cur == "right":
            arr[i][j] = loc
            j += 1
            if j == n or arr[i][j] != None:
                i+=1
                j-=1
                cnt+=1
                continue
        elif cur == "down":
            arr[i][j]= loc
            i += 1
            if i == n or arr[i][j] != None:
                j -=1
                cnt+=1
                i -= 1
                continue
        elif cur == "left":
            arr[i][j] = loc
            j -= 1
            if j == -1 or arr[i][j] != None:
                i -= 1
                cnt += 1
                j += 1
                continue
        elif cur == "up":
            arr[i][j] = loc
            i -= 1
            if  arr[i][j] != None:
                j+=1
                cnt += 1
                i += 1
                continue
        # print(arr)
    return arr


# print(snail(5))
test = snail(6)
for width in test:
    print(width)
a = [[None for a in range(0,5)] for i in range(0,5)]
# print(a)


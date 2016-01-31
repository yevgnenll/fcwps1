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
    이 경우는 달라지지 않고 반드시 일어난다
    :param n:
    :return: 2차원 배열이든 1차원 배열이든 위와같은 값이 나와야 한다.
    """

    arr = [[None for a in range(0,n)] for i in range(0, n)]
    status = ["right", "down", "left", "up"] #4가지 경우
    cnt = 0 # 방향이 바뀐 횟수
    cur = status[cnt%4] # 현재 어느방향인지
    i, j = 0, 0 # 2차원 배열 인덱스 0<= i,j <= n-1
    for loc in range(1, n*n+1):

        # 현재상태 최신화
        cur =status[cnt%4]

        # 오른쪽으로 가는 경우
        if cur == "right":
            #값을 할당함
            arr[i][j] = loc
            #오른쪽으로 한칸 더 간다
            j += 1
            # 맨 끝에 도착했거나 이동한 칸에 값이 있다면 다음 상황으로 가야한다
            if j == n or arr[i][j] != None:
                # 오른쪽 이동 후에는 반드시 아래로 간다
                i+=1
                # 이미 값이 있는 장소이거나, out of range 이므로 원위치로 돌아온다
                j-=1
                # 방향이 바뀐 횟수 업데이트
                cnt+=1
                # for문 다시 시작
                continue

        # 아래로 내려가는 경우
        elif cur == "down":
            # 값을 할당한다
            arr[i][j]= loc
            # 아래로 한 칸 이동한다
            i += 1
            # 제일 아래로 왔거나 밑에 칸이 지나갔던 칸이여서 이미 값이 있는경우
            if i == n or arr[i][j] != None:
                # 아래로 이동 후에는 반드시 왼쪽으로 간다, 왼쪽으로 가는 첫번째 칸으로 이동
                j -=1
                # 방향을 바꿔주고
                cnt+=1
                # 현재 위치는 값이 있거나 out of range이므로 원래 행으로
                i -= 1
                continue
        # 왼쪽으로 가는 경우
        elif cur == "left":
            # 값을 할당한다
            arr[i][j] = loc
            # 왼쪽으로 한 칸 이동
            j -= 1

            # 왼쪽의 끝을 벗어났거나, 왼쪽칸이 지나간 곳이라 값이 있다면
            if j == -1 or arr[i][j] != None:
                # 왼쪽 이동 후는 반드시 위로 올라가므로 방향을 바꾸고
                i -= 1
                # 방향 바꾼 횟수를 증가시켜 상태를 변경하고
                cnt += 1
                # out of range이거나 이미 값이 있는 열이므로 원래 열로 돌아온다
                j += 1
                continue
        # 위로 올라가는 경우
        elif cur == "up":
            # 값을 할당한다
            arr[i][j] = loc
            # 위로 한 칸 올라간다
            i -= 1
            # 위로 올라가는 경우엔 out of index가 절대로 발생하지 않으므로
            # 위 칸에 이미 숫자가 있는지만 확인하여 이미 있는 경우에는
            if  arr[i][j] != None:
                # 오른쪽으로 가기 위한 준비를 하고
                j+=1
                # 방향을 바꾸고
                cnt += 1
                # 윗 칸엔 값이 있으므로 다시 원래 칸으로 내려온다
                i += 1
                continue
        # print(arr)
    return arr


# print(snail(5))
test = snail(5)
for width in test:
    print(width)
a = [[None for a in range(0,5)] for i in range(0,5)]
# print(a)

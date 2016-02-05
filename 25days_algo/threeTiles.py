#https://www.acmicpc.net/problem/2133
# 규칙
# 반드시 tiles[i-2]*3이 들어간다
# 그 다음부터는 tiles[i-2*i]*2가 더해진다
# 그런데 n이 1, 3, 5 즉 1*3, 3*3의 타일이 채워질 경우는 없다! (잘못된 가설)
# (수정 된 가설) n이 홀수인 경우 0이 오는게 맞음 1개 짜리를 채울 방법이 없다
# 계산의 편의를 위해 n=0 인 경우에는 1을 할당한다
# 조건: 1 <= n <= 30 30보다 큰 수는 들어오지 않는다
n = int(input())
tiles = [0 for _ in range(0,31)]
# 0으로 놓는 이유는 반드시 0이 들어가야 하는 n이 있기 때문
tiles[0] = 1
# n은 내가 원하는 칸 까지 돈다

# 점화식: tiles[i] = tiles[i-2]*3 + tiles[i-4]*2 + tiles[i-6] * 2 + ....
for i in range(2, n+1):
    tiles[i] = tiles[i-2] * 3
    # 그 아래 *2 해야 하는 거
    for j in range(i-4, -1, -2):
        # tiles[4] = tiles[2]*3에서 끝난 이유
        # range(i-4, 0, -2) 이면 i가 4인경우 절대로 두번째 for를 타지 않음
        # range(i-4, -1,-2) 로 해야 tiles[0]까지 계산함
        tiles[i] += tiles[j] * 2
print(tiles[n])
# print(tiles) 완료
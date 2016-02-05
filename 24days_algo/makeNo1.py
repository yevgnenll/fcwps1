makeNo = int(input())
cnt = 0
num = makeNo
#    x 1  2  3, 4
dp = [0,0, 1, 1]

for i in range(4, makeNo+1):

    if i%2 == 0 and i%3 ==0:
        dp.append(min(dp[i-1], dp[i//3], dp[i//2])+1)

    elif i%3 ==0:
        dp.append(min(dp[i-1], dp[i//3])+1)

    elif i%2 ==0:
        dp.append(min(dp[i-1], dp[i//2])+1)

    else:
        dp.append(dp[i-1]+1)


print(dp[-1])
# print(dp[makeNo-1])
#
# print("res:",dp[makeNo-1], len(dp))
# print("dps:",dp)



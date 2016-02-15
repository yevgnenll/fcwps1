#https://www.acmicpc.net/problem/6588
n = 1000000
# prime = [False for n in range(n+1)]
# # 소수는 2부터
# prime[1]= True
# for i in range(2, n):
#     if prime[i]:
#         continue
#     # 소수가 아닌걸 찾아낸다,
#     # 2의배수 3의배수, i의 배수를 모두 찾아내서 True로 둔다
#     for j in range(i*i, n+1, i):
#         # print("i: %s, j: %s"%(i,j))
#         prime[j] = True
# res = list()
# for idx, p in enumerate(prime):
#     if not p:
#         res.append(idx)
#
#
# while True:
#     user = int(input())
#     if user == 0:
#         break
#     print(prime[user]) # 이걸로 소수인지 아닌지 알 수 있다
#     print(res[user])

check = [False for i in range(n+1)]
# 체크를 위한 리스트로 모든 자리는 True 아니면 False이다
check[1] = True
primes = []
for i in range(2, n+1):
    if check[i]:
        continue
    primes.append(i)
    for j in range(i*i, n+1, i):
        check[j] = True
# print(primes)
while True:
    n = int(input())
    if n == 0:
        break

    for prime in primes:
        # prime + ? = n

        if check[n-prime] == False:
            print("%d = %d + %d"%(n, prime, n-prime))
            # print(check[n-prime], check[prime], prime, n, n-prime)


            # break

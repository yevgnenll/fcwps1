#https://www.acmicpc.net/problem/1929
# start, end = map(int, input().split())

# index가 숫자이고 소수이면 True, 아니면 False

def isPrime(number):
    """
    number가 소수라면 True 아니면 False
    2~루트 number까지만 모두 나누어보면 된다
    """
    if number < 2:
        return False
    else:
        i = 2
        while True:
            if i * i <= number:
                if number % i == 0:
                    return False
            else:
                return True
            i += 1
def findPrimes(m, n):
    """
    좀 더 사고를 유연하게 해야할 필요가 있다,
    list라고 해서 값만 사용하는게 아니라 index를 사용하는 경우이다
    사고의 틀을 좀 더 유연하게 하자
    :param m:
    :param n:
    :return:
    """
    prime = [False for n in range(n+1)]
    # 소수는 2부터
    prime[1]= True
    for i in range(2, n):
        if prime[i]:
            continue
        # 소수가 아닌걸 찾아낸다,
        # 2의배수 3의배수, i의 배수를 모두 찾아내서 True로 둔다
        for j in range(i*i, n+1, i):
            # print("i: %s, j: %s"%(i,j))
            prime[j] = True
    res = list()
    for idx, p in enumerate(prime):
        if not p:
            res.append(idx)
    return res
print(findPrimes(1,50))











#
# for idx,num in enumerate(a):
#     if num == 1:
#         a[idx] = None
#     if num % 2 ==0 and num//2>1:
#         a[idx] = None
#     elif num % 3 ==0 and num//3 >1:
#         a[idx] = None
#     elif num % 5 ==0 and num//5 >1:
#         a[idx] = None
#     elif num % 7 == 0 and num // 7 >1:
#         a[idx] = None
# print(a)




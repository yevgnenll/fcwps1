#https://www.acmicpc.net/problem/11653
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
number = int(input())
resVal = ""
isEnd = True
if isPrime(number):
    isEnd=False
    resVal += str(number)
if number >= 25:
    n = int(number**0.6)
    # n = number-1
else:
    n = int(number)

check = [False for i in range(n+1)]
check[1] = True
primes = list()


for i in range(2, n+1):
    if check[i]:
        continue
    primes.append(i)
    for j in range(i*i, n+1, i):
        check[j] = True
# print("len", len(primes))

while isEnd:
    if number % primes[0] == 0:
        resVal += str(primes[0])+"\n"
        number //= primes[0]
        if number == 1:
            isEnd = False
    else:
        del primes[0]
print(resVal.strip("\n"))

def kthDivisor(n, k):
    res = list()
    for num in range(1, n+1):
        if n % num == 0:
            res.append(num)

    print(res)

    if len(res) < k:
        return -1
    else :
        return res[k-1]

def quasifactorial(n):
    if n == 1:
        return 1

    return quasifactorial(n-1) * n -1

print(quasifactorial(4))

def maxNumberOfDivisorsPermutation(n):
    res= list()


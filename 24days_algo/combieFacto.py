#https://www.acmicpc.net/problem/2004



# facto = int(input())


def facto(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def combie(m, n):
    return facto(m)//(facto(n)*facto(m-n))

print(combie(25,12))


def enhancedCombie(m, n):
    up = 1
# a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(a, a%b)

print(gcd(12, 90))


def isSumOfConsecutive2(n):
    mid = list()
    for i in range(n):
        mid.append(i)
    print(mid)
    sum = 0
    result =0
    start =0
    while True:
        for s in mid[start:]:
            sum += s
            print(start, sum, s)
            if sum == n:
                print("sum == n")
                result += 1
                start += 1
                break
            if sum > n:
                print("sum > n")
                sum =0
                start += 1
                break
            if start == n or start > n:
                print("start == n or start > 0")
                break
        if start == n-1:
            break

    return result

print("result",isSumOfConsecutive2(3))


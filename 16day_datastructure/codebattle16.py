def greetPerson(name):
    return "Hello, "+name

def numberOfTriangles2(sticks):
    first = list()
    mid = list()
    for i in range(len(sticks)):
        sticks[i]



def digitDegree(n):
    num = str(n)
    sum = 0
    count =0
    while True:
        if n < 10:
            break
        for a in num:
            sum += int(a)
        if sum < 10:
            count += 1
            break
        else:
            print(sum)
            num = str(sum)
            sum = 0
            count += 1

    return count

def digitSumInverse(sum, numberLength):
    limit = 10 ** numberLength-1
    result = list()
    for num in range(1,limit+2):
        mid = str(num)
        all =0
        i =0
        isCheck = False
        print("mid",mid)
        for a in mid:
            all += int(a)
            print(mid, a, all, i,"sum:", sum)
            if all == sum:
                print(all)
                result.append(mid)
            print("--")
    print(result)
    count =0
    for a in result:
        m = str(a)
        to = 0
        for l in m:
            to += int(l)
            if to == sum:
                count += 1

    return count

print(digitSumInverse(5, 2))






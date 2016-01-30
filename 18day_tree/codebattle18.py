def isLuckyNumber(n):
    num = str(n)
    isFour = False
    isSeven = False
    for i in num:
        if i == "4":
            isFour = True
            print(i, isFour)
        elif i == "7":
            isSeven = True
            print(i, isSeven)
    if isSeven == True and isFour == True:
        return True
    else:
        return False

def sumOfDivisors(n):
    sum = 0
    for a in range(1, n+1):
        if n % a == 0:
            sum += a
    return sum

def properNounCorrection(noun):
    return str(noun).capitalize()

def mySubstring(inputString, l, r):
    return inputString[l:r+1]

def toAndFro(a, b, t):
    dis = b -a
    location = 2
    for loc in range(1, t+1):
        if dis >= location:
            location += 1
        elif a < location:
            location -=1

        print(location)

    return location

# print("result", toAndFro(1,10,8))

def matrixnum(matrix):
    res = list()
    for a in matrix:
        mid = list()
        mid.append(a)
        for j in a:
            mid.append(j)
    res.append(mid)
    return res

print(matrixnum([[1, 1, 3],
                     [2, 1, 1]]))



def find(k):
    num = str(k)
    odd = 0
    even = 0
    for n in num:
        if int(n) % 2 == 0:
            even += int(n)
        else :
            odd += int(n)
    return even-odd

print(find(1203))


#range인자 갯수 상관없게 만들어보자
def flexibleArgRange(*args):
    """
    range 함수 만들기
    :param args:
        1. (end)
        2. (start, end)
        3. (start, end, step)
    :return:
    """
    start =0
    num =start
    stop =0
    step = 1
    result = list()
    if len(args) == 0:
        return "뭘 입력해줘야..."
    elif len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        return "입력한 매개변수 갯수를 확인해주세요"

    if step > 0:
        if start > stop:
            return "step에 +를 넣으면 숫자가 작아질 수 없어 ㅜㅜ"
        while num < stop:
            result.append(num)
            num += step
    elif step < 0:
        if start < stop and step < 0:
            return "-를 넣으면 절대로 숫자가 올라갈수 없어 ㅜ"
        else:
            last = start
            while last > stop:
                result.append(num)
                num += step
                last = num
                #print("num:", num, "last:", last)
    else:
        return "step은 0보다 크거나 작아야합니다"

print(flexibleArgRange(0,10,1))


#def enhancedRange(start=0, stop, step =1):



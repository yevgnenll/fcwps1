import time
import sys
def elapsed_time(func):
    def elsapse(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("============================================================================")
        print("함수이름:",func.__name__)
        print("걸린시간:",(end - start)/(24*60*60*1000) ,"초")
        if len(args) >0:
            print("들어온값:", args)
        if len(kwargs):
            print("들어온 값:", kwargs)
        print("이 함수로 실행할 결과:", result)
        print("============================================================================")
        return result
    return elsapse



@elapsed_time
def testForElaTiem(n):
    res = list()
    for count in range(n):
        res.append(count)

    print(locals())
    return len(res)

testForElaTiem(5)
for place in sys.path:
    print(place)


# 100개 0.004초
# 1000개 0.020초
# 10000개 0.265초
# 50000개 1.117초
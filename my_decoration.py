import time

class MyDecoration():
    def logDecoration(self, func):
        def elasped_time(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("============================================================================")
            print("함수이름:", func.__name__)
            if len(args) > 0:
                print("매개변수:", args)
            if len(**kwargs) > 0 :
                print("매개벼수", kwargs)
            print("걸린시간", (end- start)/ 1000, "초")
            if result is not None:
                print("실행결과:", result)
                return result
            print("============================================================================")
        return elasped_time()


class testFile():
    def writeTest(self, text, path):
        with open(text, "wt") as streamText:
            streamText.write(text)


a= "(1+2)*4*(6/2)-1" #35
print("result",eval(a))
# exec()
print(exec.__doc__)
print("---------")
print("eval\n", eval.__doc__)

import time

def elapsed_time(func):
    def elsapse(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("============================================================================")
        print("함수이름:",func.__name__)
        print("걸린시간:",(end - start)*1000,"초")
        # print("걸린시간:",(end - start)/24*60*60 ,"초")
        if len(args) >0:
            print("들어온값:", args)
        if len(kwargs):
            print("들어온 값:", kwargs)
        print("리턴타입:", type(result))
        print("실행결과:", result)
        print("함수문서", func.__doc__)
        print("============================================================================")

        if result is None:
            return None

        return result
    return elsapse

class readFile():

    test = "1234"
    @elapsed_time
    def readMyFile(self,path,mode):
        txt = open(path, mode)
        result = txt.read()
        txt.close()
        return result

    @elapsed_time
    def readWordCount(self, path, mode, count):
        data = open(path, mode)
        txt = data.read() #왜 에러가 발생할까??
        size = len(txt)
        offset = 0
        chuck = count
        result = list()
        while offset < size:
            # print(txt[offset:offset + chuck])
            result.append(txt[offset:offset + chuck])
            offset += chuck
        data.close()
        return result

    @elapsed_time
    def readTextLine(self, path, mode):
        data = open(path, mode)
        result = list()
        while True:
            text = data.readline()
            if not text:
                break
            result.append(text)
        data.close()
        return result

    @elapsed_time
    def writeBin(self,path, end):
        bin_data = bytes(range(end))
        res = open(path, "wb")
        res.write(bin_data)
        res.close()

    @elapsed_time
    def readBin(self, path):
        bin_txt = open(path, "rb")
        result = bin_txt.read()
        bin_txt.close()
        return result

mypath ='/Users/yevgnenll/Desktop/'
fileIO = readFile()
# result = fileIO.readTextLine(mypath+"fileio.txt", "rt")
fileIO.writeBin(mypath+"bin.txt",256)
# binResult = fileIO.readBin(mypath+"bin.txt")
# print(result)



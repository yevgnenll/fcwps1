from pytube import YouTube

# youtube("https://www.youtube.com/watch?v=22mdHYEzKC0","Paint")

yt = YouTube("https://www.youtube.com/watch?v=22mdHYEzKC0")
yt.set_filename("paint")
video = yt.get('mp4','720p')
video.download('/Users/yevgnenll/Desktop/')
"""
def plus(a,b):
    return a,b

def minus(c, d):
    return c - d

g = lambda x, y : x*y


h = lambda a,b,c,d: plus(a,b)+minus(c,d)

print(h(1,1,3,2))
"""
# def countdown(n):
#     print('counting down %d' %n)
#     while n > 0:
#         yield n # 10을 바로 리턴하고 여기서 멈춤.
#         n -= 1
#     return
#
# c = countdown(10) #c로 치면 포인터 개념임.
# c.__next__()
# c.__next__()
# c.__next__()
# c.__next__()
# c.__next__()
# c.__next__()
# c.__next__()

#print(c.__next__())
#print(type(c))
#print(type(countdown(10)))
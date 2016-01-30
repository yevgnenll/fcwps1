"""
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=roeGKaU-MeM")
yt.set_filename("zeze iu")
video = yt.get("mp4", "720p")
video.download("/Users/yevgnenll/Desktop")
"""
#a ="sdf"

a = ['cd','gh','ef', 'ab']
c = a
c.sort()
b = sorted(a)
print (a, b, c)

ab = "abcdfghijklmnopqrstuvwxyz"
print(ab[-4:-20:-4])
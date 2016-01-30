from pytube import YouTube

# youtube("https://www.youtube.com/watch?v=22mdHYEzKC0","Paint")

yt = YouTube("https://www.youtube.com/watch?v=22mdHYEzKC0")
yt.set_filename("paint")
video = yt.get('mp4','720p')
video.download('/Users/yevgnenll/Desktop/')

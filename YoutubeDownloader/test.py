import pytube
from pytube import YouTube

video=YouTube("https://www.youtube.com/watch?v=qk2WMmiiVFE")
#x=["https://www.youtube.com/watch?v=rMQ_TUEwQEs","https://www.youtube.com/watch?v=qk2WMmiiVFE"]

#print(video.streams.all)
print("Downloading...")
video=video.streams.all

print(video)




#streamslist=video.streams.all
#print(streamslist.title(),"  ",streamslist.views()," ",streamslist.length())
"""for video in x:
    print(YouTube(video).title," ",YouTube(video).views," ",YouTube(video).length)



print(type(streamslist))
s=str(streamslist)
print(s)
l1=list()
l1.append(s)
print(l1)"""

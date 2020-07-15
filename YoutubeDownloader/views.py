from django.http import HttpResponse
from django.shortcuts import render
import json
from pytube import YouTube
import datetime,time


dict={}
def index(request):
    print(request.POST)
    if request.method=="POST" and 'Submit1' in request.POST:
        print("Entered Submit1")
        link=request.POST.get('urllink','')
        video=YouTube(link)
        title=video.title
        duration=video.length
        duration=str(datetime.timedelta(seconds = duration))
        views=video.views
        print(title,views,duration)
        vs=video.streams.filter(progressive="True")
        vs=str(vs)
        listgen = vs.split("Stream:")
        #dict={}
        global dict
        print(len(listgen))
        for x in listgen[1:]:
            res=findres(x)
            tag=findtag(x)
            dict[tag]=res
        print("DICT is: ",dict)
        param={'link':link,'title':title,'duration':duration,'views':views,'dict':dict}
        return HttpResponse(json.dumps(param))
    elif  request.method=="POST" and 'Submit2' in request.POST:
        print("Entered SUbmit 2")
        url = request.POST.get('videourl', '')
        print("url is :", url)
        path = request.POST.get('Downloadpath', '')
        res = request.POST.get('selectreso', '')
        print("RESOLUTION :",res)
        #dict = request.POST.get('dict', '')
        print("dict is :",dict)
        #innerdict = json.loads(dict)
        key_list = list(dict.keys())
        val_list = list(dict.values())
        itag = key_list[val_list.index(res)]
        print(itag)
        video = YouTube(url)
        time.sleep(2)
        # if path=="":
        #     video.streams.get_by_itag(itag).download(path)
        # else:
        #     video.streams.get_by_itag(itag).download(path)
        return HttpResponse(json.dumps({'thank': True}))
    else:
        return render(request,'home.html')

def contact(request):
    return render(request,'aboutus.html')


def findres(data):
    val = data.find("res=")
    val2 = data[val + 5:]
    val2 = val2.find('"')
    res = data[val + 5:val + 5 + val2]
    return res

def findtag(data):
    val = data.find("itag=")
    val2 = data[val + 6:]
    val2 = val2.find('"')
    res = data[val + 6:val + 6 + val2]
    return res







import os, json, re, urllib.request
from pytube import YouTube
from .models import Slider


def api_slider():
    api_key = os.environ.get('API_KEY')
    channel_id = "UCJymPbg-0_yc-63wqc0WtIQ"
    twelve_videos = []
    twelve_videos_url = ['https://www.youtube.com/watch?v=' for i in range(12)]

    temp_lst = []
    end_lst = []
    count = 0

    list_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=12&order=date&type=video&key={api_key}"
    json_url = urllib.request.urlopen(list_url)
    data = json.loads(json_url.read())
    for i in data['items']:
        twelve_videos_url[count] += str(i['id']['videoId'])
        twelve_videos.append(f"https://img.youtube.com/vi/{str(i['id']['videoId'])}/maxresdefault.jpg")
        count += 1
    for i in range(12):
        temp_lst.append(twelve_videos_url[i])
        try:
            temp_lst.append(twelve_videos[i])
        except:
            temp_lst.append('')
        end_lst.append(temp_lst)
        temp_lst = []

    return end_lst


def update_slider():
    for i in range(12):
        lst = api_slider()
        temp = Slider.objects.get(id=i + 1)
        if lst[i][1] == "":
            temp.img_url = "/static/img/nothing.png"
            temp.url = "#"
        else:
            temp.url = lst[i][0]
            temp.img_url = lst[i][1]
        temp.save()


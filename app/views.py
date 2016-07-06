from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def tab_detail_view(request, url):
    tab_url = "http://www.bigbasstabs.com/" + url
    content = requests.get(tab_url).text
    souper = BeautifulSoup(content, "html.parser")
    results = str(souper.find(class_="song"))

    return render(request, "detail.html", {"results": results})


def tab_search_view(request):
    if request.GET.get("artist"):
        artist = request.GET.get("artist").lower().replace(" ", "_")
        letter = artist[0]
        url = "http://www.bigbasstabs.com/{}/{}_bass_tabs.html".format(letter, artist)
        content = requests.get(url).text
        souper = BeautifulSoup(content, "html.parser")
        #print(souper.find(id="content").find())
        results = str(souper.find(class_="song-list"))

        return render(request, "index.html", {"results": results, "artist": artist})

    elif request.GET.get("song"):
        song = request.GET.get("song").lower().replace(" ", "_")
        url = "http://www.bigbasstabs.com/search.html?search={}&type=songs".format(song)
        content = requests.get(url).text
        souper = BeautifulSoup(content, "html.parser")
        results = str(souper.find(class_="song-list"))

        return render(request, "index.html", {"results": results, "song": song})

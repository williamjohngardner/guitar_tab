from django.shortcuts import render
import requests
from bs4 import BeautifulSoup




def tab_search_view(request):
    artist = request.GET.get("artist")
    letter = artist[0]
    url = "http://www.bigbasstabs.com/{}/{}_bass_tabs.html".format(letter, artist)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    results = souper.find_all(class_="song-list")

    return render(request, "index.html", {"results": results})

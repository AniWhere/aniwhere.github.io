from django.shortcuts import render,redirect
from .models import Bookmark

import json

def main(request):
    return render(request,"main.html")

def bookmark(request):
    bookmarks=Bookmark.objects
    return render(request,"bookmark.html",{'bookmarks':bookmarks})


def check(request,id):
    bookmark = Bookmark.objects.get(id=id)
    if bookmark.star is 1:
        bookmark.star = 0
    else:
        bookmark.star = 1
    bookmark.save()
    return redirect('recommend')
    
def plan(request):
    return render(request,"plan.html")

def recommend(request):
    bookmarks=Bookmark.objects
    return render(request,"recommend.html",{'bookmarks':bookmarks})

def showattractions(request):
    with open('static/json/example.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)['response']['body']['items']['item']

    attractiondict = []
    for attraction in attractions:
            content = {
                "title": attraction['title'],
                "mapx": str(attraction['mapx']),
                "mapy": str(attraction['mapy']),
                "addr1": str(attraction['addr1']),
            }
            if attraction.get('tel'):
                content['tel'] = str(attraction['tel'])
            else:
                content['tel'] = ''
            attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'board.html', {'attractionJson': attractionJson})

def search(request):
    with open('static/json/example.json', encoding='utf-8') as json_file:
        attractions = json.load(json_file)['response']['body']['items']['item']
    search_keyword= request.GET.get('key')
    search_city= request.GET.get('city')
    attractiondict = []

    for attraction in attractions:
        if attraction.get('keyword')==search_keyword:
            if ((attraction.get('addr1')).find(search_city)!=-1 or search_city=="지역"):
                content = {
                    "title": attraction['title'],
                    "mapx": str(attraction['mapx']),
                    "mapy": str(attraction['mapy']),
                    "addr1": str(attraction['addr1']),
                }
                if attraction.get('tel'):
                    content['tel'] = str(attraction['tel'])
                else:
                    content['tel'] = ''
                attractiondict.append(content)
        elif search_keyword=='':
            if ((attraction.get('addr1')).find(search_city)!=-1 or search_city=="지역"):
                content = {
                    "title": attraction['title'],
                    "mapx": str(attraction['mapx']),
                    "mapy": str(attraction['mapy']),
                    "addr1": str(attraction['addr1']),
                }
                if attraction.get('tel'):
                    content['tel'] = str(attraction['tel'])
                else:
                    content['tel'] = ''
                attractiondict.append(content)
    attractionJson = json.dumps(attractiondict, ensure_ascii=False)
    return render(request, 'board.html', {'attractionJson': attractionJson})
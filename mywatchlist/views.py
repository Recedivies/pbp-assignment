from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_html(request):
    data = MyWatchList.objects.all()
    return render(request, "mywatchlist.html", {"watch_list": data})


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )

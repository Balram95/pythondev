
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    albums=Album.objects.all()
    return render(request,'./music/index.html',{'albums':albums})

def details(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except DoesNotExist:
        raise Http404('No')
    return render(request,'./music/details.html',{'album':album})

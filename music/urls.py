from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="music"
urlpatterns = [
    # will go to /music
    url(r'^$', views.index,name="index"),
    url(r'^(?P<album_id>[0-9]+)/$', views.details ,name="details"),
]

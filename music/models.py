# -*- coding: utf-8 -*-


# dp = models.ImageField(upload_to = getdpPath , null = True)
# email = models.BooleanField(default = False)
# created = models.DateTimeField(auto_now_add = True)
# attachment = models.FileField(upload_to = getSupportChatAttachment , null = True)
# responseTime = models.FloatField(null=True, blank=True)
# email = models.EmailField(null = True)
# chatedDate = models.DateField(null=True)



from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + '-' + self.country

class Album(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)
    releasedate=models.DateField(null=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title + '-' + self.type

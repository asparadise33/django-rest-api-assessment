from django.db import models
from .artist import Artist
#from .genre import Genre

class Song(models.Model):

    title = models.TextField(max_length=60)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    album = models.TextField(max_length=80)
    length = models.IntegerField(max_length=270)
    #genres = models.ManyToManyField(Genre)

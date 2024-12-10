from django.db import models
from .song import Song

class Genre(models.Model):

  description = models.TextField(max_length=45)
  songs = models.ManyToManyField(Song, through='SongGenre', related_name='songs')

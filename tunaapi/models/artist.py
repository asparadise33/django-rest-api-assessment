from django.db import models

class Artist(models.Model):

    name = models.CharField(max_length=45)
    age = models.IntegerField(max_length=100)
    bio = models.TextField(max_length=150)

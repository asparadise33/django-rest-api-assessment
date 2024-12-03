from django.db import models

class Genre(models.Model):

  description = models.TextField(max_length=45)

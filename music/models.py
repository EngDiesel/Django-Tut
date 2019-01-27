from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + " - " + self.artist


class Song(models.Model):
    title = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

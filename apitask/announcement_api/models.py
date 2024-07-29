from django.db import models


class Announcement(models.Model):
    header = models.CharField(max_length=300)
    author = models.CharField(max_length=60)
    views_count = models.IntegerField()
    position = models.IntegerField()